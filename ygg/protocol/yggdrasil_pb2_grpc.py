# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import yggdrasil_pb2 as yggdrasil__pb2


class DispatcherStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/yggdrasil.Dispatcher/Register',
                request_serializer=yggdrasil__pb2.RegisterRequest.SerializeToString,
                response_deserializer=yggdrasil__pb2.RegisterResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/yggdrasil.Dispatcher/Update',
                request_serializer=yggdrasil__pb2.Assignment.SerializeToString,
                response_deserializer=yggdrasil__pb2.Empty.FromString,
                )
        self.Finish = channel.unary_unary(
                '/yggdrasil.Dispatcher/Finish',
                request_serializer=yggdrasil__pb2.Assignment.SerializeToString,
                response_deserializer=yggdrasil__pb2.Empty.FromString,
                )


class DispatcherServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Register is called by a worker to indicate it is ready and capable of
        handling the specified type of work.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update can be called by a worker if it wants to submit some output,
        but has not completed the assigned work.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Finish(self, request, context):
        """Finish is called by a worker when it has completed its assigned work.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DispatcherServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=yggdrasil__pb2.RegisterRequest.FromString,
                    response_serializer=yggdrasil__pb2.RegisterResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yggdrasil__pb2.Assignment.FromString,
                    response_serializer=yggdrasil__pb2.Empty.SerializeToString,
            ),
            'Finish': grpc.unary_unary_rpc_method_handler(
                    servicer.Finish,
                    request_deserializer=yggdrasil__pb2.Assignment.FromString,
                    response_serializer=yggdrasil__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yggdrasil.Dispatcher', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Dispatcher(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yggdrasil.Dispatcher/Register',
            yggdrasil__pb2.RegisterRequest.SerializeToString,
            yggdrasil__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yggdrasil.Dispatcher/Update',
            yggdrasil__pb2.Assignment.SerializeToString,
            yggdrasil__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Finish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yggdrasil.Dispatcher/Finish',
            yggdrasil__pb2.Assignment.SerializeToString,
            yggdrasil__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class WorkerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Start = channel.unary_unary(
                '/yggdrasil.Worker/Start',
                request_serializer=yggdrasil__pb2.Assignment.SerializeToString,
                response_deserializer=yggdrasil__pb2.StartResponse.FromString,
                )
        self.Status = channel.unary_unary(
                '/yggdrasil.Worker/Status',
                request_serializer=yggdrasil__pb2.Empty.SerializeToString,
                response_deserializer=yggdrasil__pb2.WorkerStatus.FromString,
                )


class WorkerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Start(self, request, context):
        """Start is called by the manager to assign work to a worker.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Status(self, request, context):
        """Status is called by the manager to check whether or not a worker is busy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=yggdrasil__pb2.Assignment.FromString,
                    response_serializer=yggdrasil__pb2.StartResponse.SerializeToString,
            ),
            'Status': grpc.unary_unary_rpc_method_handler(
                    servicer.Status,
                    request_deserializer=yggdrasil__pb2.Empty.FromString,
                    response_serializer=yggdrasil__pb2.WorkerStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yggdrasil.Worker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Worker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yggdrasil.Worker/Start',
            yggdrasil__pb2.Assignment.SerializeToString,
            yggdrasil__pb2.StartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yggdrasil.Worker/Status',
            yggdrasil__pb2.Empty.SerializeToString,
            yggdrasil__pb2.WorkerStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
