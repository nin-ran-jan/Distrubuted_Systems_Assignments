# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import buyer_pb2 as buyer__pb2


class BuyerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RateProduct = channel.unary_unary(
                '/ecommerce.Buyer/RateProduct',
                request_serializer=buyer__pb2.RateProductRequest.SerializeToString,
                response_deserializer=buyer__pb2.RateProductResponse.FromString,
                )


class BuyerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BuyerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.RateProduct,
                    request_deserializer=buyer__pb2.RateProductRequest.FromString,
                    response_serializer=buyer__pb2.RateProductResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ecommerce.Buyer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Buyer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce.Buyer/RateProduct',
            buyer__pb2.RateProductRequest.SerializeToString,
            buyer__pb2.RateProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
