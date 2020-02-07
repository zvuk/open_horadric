"""
Generated by open_horadric. DO NOT EDIT!
"""

from __future__ import annotations

from typing import Iterable

from open_horadric_lib.base.context import Context
from open_horadric_lib.server.base_interface import BaseServerInterface
from open_horadric_lib.server.middleware.base import apply_middlewares
import grpc

from example_py3.foo.bar.messages import TestMessage
import example_py3.google.protobuf.messages

__all__ = ('TestServiceInterface',)


class TestServiceInterface(BaseServerInterface):
    def _test_method(self, request: TestMessage, context: Context) -> TestMessage.TestNestedMessage:
        context.service_name = "TestService"
        context.method_name = "TestMethod"
        return self.test_method(request=request, context=context)

    def _client_streaming(self, request: Iterable[TestMessage], context: Context) -> TestMessage.TestNestedMessage:
        context.service_name = "TestService"
        context.method_name = "ClientStreaming"
        return self.client_streaming(request=request, context=context)

    def _server_streaming(self, request: TestMessage, context: Context) -> Iterable[TestMessage.TestNestedMessage]:
        context.service_name = "TestService"
        context.method_name = "ServerStreaming"
        return self.server_streaming(request=request, context=context)

    def _client_server_streaming(self, request: Iterable[TestMessage.TestNestedMessage], context: Context) -> Iterable[TestMessage.TestNestedMessage]:
        context.service_name = "TestService"
        context.method_name = "ClientServerStreaming"
        return self.client_server_streaming(request=request, context=context)

    def _empty_method(self, request: example_py3.google.protobuf.messages.Empty, context: Context) -> example_py3.google.protobuf.messages.Empty:
        context.service_name = "TestService"
        context.method_name = "EmptyMethod"
        return self.empty_method(request=request, context=context)

    def test_method(self, request: TestMessage, context: Context) -> TestMessage.TestNestedMessage:
        raise NotImplementedError

    def client_streaming(self, request: Iterable[TestMessage], context: Context) -> TestMessage.TestNestedMessage:
        raise NotImplementedError

    def server_streaming(self, request: TestMessage, context: Context) -> Iterable[TestMessage.TestNestedMessage]:
        raise NotImplementedError

    def client_server_streaming(self, request: Iterable[TestMessage.TestNestedMessage], context: Context) -> Iterable[TestMessage.TestNestedMessage]:
        raise NotImplementedError

    def empty_method(self, request: example_py3.google.protobuf.messages.Empty, context: Context) -> example_py3.google.protobuf.messages.Empty:
        raise NotImplementedError

    def bind(self, server):
        self.test_method = apply_middlewares(self.test_method, *self.middlewares)
        self.client_streaming = apply_middlewares(self.client_streaming, *self.middlewares)
        self.server_streaming = apply_middlewares(self.server_streaming, *self.middlewares)
        self.client_server_streaming = apply_middlewares(self.client_server_streaming, *self.middlewares)
        self.empty_method = apply_middlewares(self.empty_method, *self.middlewares)

        rpc_method_handlers = {
            'TestMethod': grpc.unary_unary_rpc_method_handler(
                self._wrap_method(self._test_method),
                request_deserializer=TestMessage.FromString,
                response_serializer=TestMessage.TestNestedMessage.SerializeToString,
            ),
            'ClientStreaming': grpc.stream_unary_rpc_method_handler(
                self._wrap_method(self._client_streaming),
                request_deserializer=TestMessage.FromString,
                response_serializer=TestMessage.TestNestedMessage.SerializeToString,
            ),
            'ServerStreaming': grpc.unary_stream_rpc_method_handler(
                self._wrap_method(self._server_streaming),
                request_deserializer=TestMessage.FromString,
                response_serializer=TestMessage.TestNestedMessage.SerializeToString,
            ),
            'ClientServerStreaming': grpc.stream_stream_rpc_method_handler(
                self._wrap_method(self._client_server_streaming),
                request_deserializer=TestMessage.TestNestedMessage.FromString,
                response_serializer=TestMessage.TestNestedMessage.SerializeToString,
            ),
            'EmptyMethod': grpc.unary_unary_rpc_method_handler(
                self._wrap_method(self._empty_method),
                request_deserializer=example_py3.google.protobuf.messages.Empty.FromString,
                response_serializer=example_py3.google.protobuf.messages.Empty.SerializeToString,
            ),
        }

        generic_handler = grpc.method_handlers_generic_handler('foo.bar.TestService', rpc_method_handlers)
        server.add_generic_rpc_handlers((generic_handler,))
