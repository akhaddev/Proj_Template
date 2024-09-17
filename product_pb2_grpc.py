# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import product_pb2 as product__pb2


class ProductServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateProduct = channel.unary_unary(
                '/ProductService/CreateProduct',
                request_serializer=product__pb2.CreateProductRequest.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                )
        self.GetProduct = channel.unary_unary(
                '/ProductService/GetProduct',
                request_serializer=product__pb2.GetProductRequest.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                )
        self.UpdateProduct = channel.unary_unary(
                '/ProductService/UpdateProduct',
                request_serializer=product__pb2.UpdateProductRequest.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                )
        self.DeleteProduct = channel.unary_unary(
                '/ProductService/DeleteProduct',
                request_serializer=product__pb2.DeleteProductRequest.SerializeToString,
                response_deserializer=product__pb2.EmptyResponse.FromString,
                )


class ProductServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProduct,
                    request_deserializer=product__pb2.CreateProductRequest.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'GetProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProduct,
                    request_deserializer=product__pb2.GetProductRequest.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'UpdateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProduct,
                    request_deserializer=product__pb2.UpdateProductRequest.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'DeleteProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProduct,
                    request_deserializer=product__pb2.DeleteProductRequest.FromString,
                    response_serializer=product__pb2.EmptyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/CreateProduct',
            product__pb2.CreateProductRequest.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/GetProduct',
            product__pb2.GetProductRequest.SerializeToString,
            product__pb2.ProductResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/ProductService/UpdateProduct',
            product__pb2.UpdateProductRequest.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/DeleteProduct',
            product__pb2.DeleteProductRequest.SerializeToString,
            product__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
