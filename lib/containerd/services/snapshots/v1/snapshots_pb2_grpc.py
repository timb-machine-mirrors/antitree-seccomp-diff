# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from containerd.services.snapshots.v1 import snapshots_pb2 as containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class SnapshotsStub(object):
    """Snapshot service manages snapshots
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Prepare = channel.unary_unary(
                '/containerd.services.snapshots.v1.Snapshots/Prepare',
                request_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.PrepareSnapshotRequest.SerializeToString,
                response_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.PrepareSnapshotResponse.FromString,
                )
        self.View = channel.unary_unary(
                '/containerd.services.snapshots.v1.Snapshots/View',
                request_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ViewSnapshotRequest.SerializeToString,
                response_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ViewSnapshotResponse.FromString,
                )
        self.Mounts = channel.unary_unary(
                '/containerd.services.snapshots.v1.Snapshots/Mounts',
                request_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.MountsRequest.SerializeToString,
                response_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.MountsResponse.FromString,
                )
        self.Commit = channel.unary_unary(
                '/containerd.services.snapshots.v1.Snapshots/Commit',
                request_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.CommitSnapshotRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Remove = channel.unary_unary(
                '/containerd.services.snapshots.v1.Snapshots/Remove',
                request_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.RemoveSnapshotRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Stat = channel.unary_unary(
                '/containerd.services.snapshots.v1.Snapshots/Stat',
                request_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.StatSnapshotRequest.SerializeToString,
                response_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.StatSnapshotResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/containerd.services.snapshots.v1.Snapshots/Update',
                request_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UpdateSnapshotRequest.SerializeToString,
                response_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UpdateSnapshotResponse.FromString,
                )
        self.List = channel.unary_stream(
                '/containerd.services.snapshots.v1.Snapshots/List',
                request_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ListSnapshotsRequest.SerializeToString,
                response_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ListSnapshotsResponse.FromString,
                )
        self.Usage = channel.unary_unary(
                '/containerd.services.snapshots.v1.Snapshots/Usage',
                request_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UsageRequest.SerializeToString,
                response_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UsageResponse.FromString,
                )
        self.Cleanup = channel.unary_unary(
                '/containerd.services.snapshots.v1.Snapshots/Cleanup',
                request_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.CleanupRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class SnapshotsServicer(object):
    """Snapshot service manages snapshots
    """

    def Prepare(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def View(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Mounts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Commit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Usage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Cleanup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SnapshotsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Prepare': grpc.unary_unary_rpc_method_handler(
                    servicer.Prepare,
                    request_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.PrepareSnapshotRequest.FromString,
                    response_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.PrepareSnapshotResponse.SerializeToString,
            ),
            'View': grpc.unary_unary_rpc_method_handler(
                    servicer.View,
                    request_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ViewSnapshotRequest.FromString,
                    response_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ViewSnapshotResponse.SerializeToString,
            ),
            'Mounts': grpc.unary_unary_rpc_method_handler(
                    servicer.Mounts,
                    request_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.MountsRequest.FromString,
                    response_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.MountsResponse.SerializeToString,
            ),
            'Commit': grpc.unary_unary_rpc_method_handler(
                    servicer.Commit,
                    request_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.CommitSnapshotRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.RemoveSnapshotRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Stat': grpc.unary_unary_rpc_method_handler(
                    servicer.Stat,
                    request_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.StatSnapshotRequest.FromString,
                    response_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.StatSnapshotResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UpdateSnapshotRequest.FromString,
                    response_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UpdateSnapshotResponse.SerializeToString,
            ),
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ListSnapshotsRequest.FromString,
                    response_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ListSnapshotsResponse.SerializeToString,
            ),
            'Usage': grpc.unary_unary_rpc_method_handler(
                    servicer.Usage,
                    request_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UsageRequest.FromString,
                    response_serializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UsageResponse.SerializeToString,
            ),
            'Cleanup': grpc.unary_unary_rpc_method_handler(
                    servicer.Cleanup,
                    request_deserializer=containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.CleanupRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'containerd.services.snapshots.v1.Snapshots', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Snapshots(object):
    """Snapshot service manages snapshots
    """

    @staticmethod
    def Prepare(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.snapshots.v1.Snapshots/Prepare',
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.PrepareSnapshotRequest.SerializeToString,
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.PrepareSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def View(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.snapshots.v1.Snapshots/View',
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ViewSnapshotRequest.SerializeToString,
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ViewSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Mounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.snapshots.v1.Snapshots/Mounts',
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.MountsRequest.SerializeToString,
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.MountsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Commit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.snapshots.v1.Snapshots/Commit',
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.CommitSnapshotRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.snapshots.v1.Snapshots/Remove',
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.RemoveSnapshotRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.snapshots.v1.Snapshots/Stat',
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.StatSnapshotRequest.SerializeToString,
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.StatSnapshotResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/containerd.services.snapshots.v1.Snapshots/Update',
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UpdateSnapshotRequest.SerializeToString,
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UpdateSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/containerd.services.snapshots.v1.Snapshots/List',
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ListSnapshotsRequest.SerializeToString,
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.ListSnapshotsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Usage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.snapshots.v1.Snapshots/Usage',
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UsageRequest.SerializeToString,
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.UsageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Cleanup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/containerd.services.snapshots.v1.Snapshots/Cleanup',
            containerd_dot_services_dot_snapshots_dot_v1_dot_snapshots__pb2.CleanupRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
