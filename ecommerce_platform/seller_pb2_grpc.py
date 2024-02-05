# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import seller_pb2 as seller__pb2


class SellerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterSeller = channel.unary_unary(
                '/ecommerce.Seller/RegisterSeller',
                request_serializer=seller__pb2.SellerRequest.SerializeToString,
                response_deserializer=seller__pb2.RegisterResponse.FromString,
                )
        self.AddProduct = channel.unary_unary(
                '/ecommerce.Seller/AddProduct',
                request_serializer=seller__pb2.SellerProductRequest.SerializeToString,
                response_deserializer=seller__pb2.RegisterResponse.FromString,
                )
        self.UpdateProduct = channel.unary_unary(
                '/ecommerce.Seller/UpdateProduct',
                request_serializer=seller__pb2.UpdateProductRequest.SerializeToString,
                response_deserializer=seller__pb2.RegisterResponse.FromString,
                )


class SellerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterSeller(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SellerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterSeller': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterSeller,
                    request_deserializer=seller__pb2.SellerRequest.FromString,
                    response_serializer=seller__pb2.RegisterResponse.SerializeToString,
            ),
            'AddProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.AddProduct,
                    request_deserializer=seller__pb2.SellerProductRequest.FromString,
                    response_serializer=seller__pb2.RegisterResponse.SerializeToString,
            ),
            'UpdateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProduct,
                    request_deserializer=seller__pb2.UpdateProductRequest.FromString,
                    response_serializer=seller__pb2.RegisterResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ecommerce.Seller', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Seller(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterSeller(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce.Seller/RegisterSeller',
            seller__pb2.SellerRequest.SerializeToString,
            seller__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce.Seller/AddProduct',
            seller__pb2.SellerProductRequest.SerializeToString,
            seller__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce.Seller/UpdateProduct',
            seller__pb2.UpdateProductRequest.SerializeToString,
            seller__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
