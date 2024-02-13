# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import notify_pb2 as notify__pb2


class NotifyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendNotification = channel.unary_unary(
                '/ecommerce.Notify/SendNotification',
                request_serializer=notify__pb2.Notification.SerializeToString,
                response_deserializer=notify__pb2.NotificationResponse.FromString,
                )


class NotifyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotifyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.SendNotification,
                    request_deserializer=notify__pb2.Notification.FromString,
                    response_serializer=notify__pb2.NotificationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ecommerce.Notify', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Notify(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce.Notify/SendNotification',
            notify__pb2.Notification.SerializeToString,
            notify__pb2.NotificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
