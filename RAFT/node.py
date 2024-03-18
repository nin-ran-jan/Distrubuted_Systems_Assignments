import grpc
import node_pb2
import node_pb2_grpc
from role import Role
from math import ceil

class LogEntry:
    def __init__(self,term,command) -> None:
        self.term = term
        self.command = command

class Node:
    def __init__(self,id) -> None:
        self.current_term = 0
        self.voted_for = None
        self.log = []
        self.commit_len = 0
        self.current_role = Role.FOLLOWER    
        self.current_leader = None
        self.votes_recv = set()
        self.sent_len = {}
        self.ack_len = {}
        self.id = id
        self.nodes = []
        self.channels = {}
        self.stubs = {}
    
    def introduce_nodes(self,node_ip_port):
        self.nodes = node_ip_port.keys()
        self.nodes.remove(self.node_id)
        for node_id in self.nodes:
            self.channels[node_id] = grpc.insecure_channel(node_ip_port[node_id])
            self.stubs[node_id] = node_pb2_grpc.NodeStub(self.channels[node_id])
    
    def recover_from_crash(self):
        self.current_role = Role.FOLLOWER
        self.current_leader = None
        self.votes_recv = {}
        self.sent_len = {}
        self.ack_len = {}
    
    def request_vote(self,node_id,term,candidate_id,last_log_index,last_log_term):
        response = self.stubs[node_id].RequestVote(
            node_pb2.RequestVoteRequest(term=term,candidate_id=candidate_id,
                                        last_log_index=last_log_index,last_log_term=last_log_term))
        if self.current_role == Role.CANDIDATE and self.current_term == response.term and response.vote_granted:
            self.votes_recv.add(node_id)
            if len(self.votes_recv) > ceil((len(self.nodes) + 1) / 2):
                self.current_role = Role.LEADER
                self.current_leader = self.id
                #cancel election timer
                for node_id in self.nodes:
                    self.sent_len[node_id] = len(self.log)
                    self.ack_len[node_id] = 0
                    self.replicate_log(node_id)
    
        elif response.term > self.current_term:
            self.current_term = response.term
            self.current_role = Role.FOLLOWER
            self.voted_for = None
            #cancel election timer
        
    def on_broadcast_request(self,msg):
        if self.current_role == Role.LEADER:
            self.log.append(LogEntry(self.current_term,msg))
            self.ack_len[self.id] = len(self.log)
            self.heartbeat()
        else:
            #Forward Request to Leader via FIFO
            pass
    
    def heartbeat(self):
        for node_id in self.nodes:
            self.replicate_log(node_id)
        
    def commit_log(self):
        acks = []
        min_acks = ceil((len(self.nodes) + 1) / 2)
        ready = []
        #Optimization: Store the ack_len in sorted format and use one pointer in the second loop
        for node_id in self.nodes:
            if self.ack_len[node_id] >= 1:
                acks.append(node_id)

        for i in range(1,len(self.log)):
            if len(acks) >= min_acks:
                ready.append(i)
            for node_id in acks:
                if self.ack_len[node_id] < (i+1):
                    acks.remove(node_id)
        ready_max = max(ready)
        if len(ready) != 0 and ready_max > self.commit_len and self.log[ready_max - 1].term == self.current_term:
            for i in range(self.commit_len,ready_max):
                #deliver log[i] msg to application
                pass
            self.commit_len = ready_max

    def replicate_log(self,follower_id):
        prefix_len = self.sent_len[follower_id]
        suffix = self.log[prefix_len:]
        prefix_term = 0
        if prefix_len > 0:
            prefix_term = self.log[prefix_len-1].term
        
        response = self.stubs[follower_id].LogRequest(
            node_pb2.LogRequestRequest(leader_id=self.id,term=self.current_term,
                                       prefix_len=prefix_len,prefix_term=prefix_term,
                                       leader_commit=self.commit_len,suffix=suffix))

        if response.term == self.current_term and self.current_role == Role.LEADER:
            if response.success and response.ack >= self.ack_len[follower_id]:
                self.sent_len[follower_id] = response.ack
                self.ack_len[follower_id] = response.ack
                self.commit_log()
            elif self.sent_len[follower_id] > 0:
                self.sent_len[follower_id] -= 1
                self.replicate_log(follower_id)
        elif response.term > self.current_term:
            self.current_term = response.term
            self.current_role = Role.FOLLOWER
            self.voted_for = None
            #cancel election timer

    def on_election(self):
        self.current_term += 1
        self.current_role = Role.CANDIDATE
        self.voted_for = self.id 
        self.votes_recv.add(self.id)
        last_term = 0
        if len(self.log) > 0:
            last_term = self.log[-1].term
        for node_id in self.nodes:
            self.request_vote(self,node_id,self.current_term,self.id,len(self.log),last_term)
        #start election timer
        