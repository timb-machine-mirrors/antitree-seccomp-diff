# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/services/containers/v1/containers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.vendor.gogoproto import gogo_pb2 as containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/services/containers/v1/containers.proto',
  package='containerd.services.containers.v1',
  syntax='proto3',
  serialized_options=b'ZFgithub.com/containerd/containerd/api/services/containers/v1;containers',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2containerd/services/containers/v1/containers.proto\x12!containerd.services.containers.v1\x1a&containerd/vendor/gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8a\x05\n\tContainer\x12\n\n\x02id\x18\x01 \x01(\t\x12H\n\x06labels\x18\x02 \x03(\x0b\x32\x38.containerd.services.containers.v1.Container.LabelsEntry\x12\r\n\x05image\x18\x03 \x01(\t\x12\x45\n\x07runtime\x18\x04 \x01(\x0b\x32\x34.containerd.services.containers.v1.Container.Runtime\x12\"\n\x04spec\x18\x05 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x13\n\x0bsnapshotter\x18\x06 \x01(\t\x12\x14\n\x0csnapshot_key\x18\x07 \x01(\t\x12\x38\n\ncreated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12\x38\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12V\n\nextensions\x18\n \x03(\x0b\x32<.containerd.services.containers.v1.Container.ExtensionsEntryB\x04\xc8\xde\x1f\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a>\n\x07Runtime\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x07options\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x1aG\n\x0f\x45xtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"!\n\x13GetContainerRequest\x12\n\n\x02id\x18\x01 \x01(\t\"]\n\x14GetContainerResponse\x12\x45\n\tcontainer\x18\x01 \x01(\x0b\x32,.containerd.services.containers.v1.ContainerB\x04\xc8\xde\x1f\x00\"(\n\x15ListContainersRequest\x12\x0f\n\x07\x66ilters\x18\x01 \x03(\t\"`\n\x16ListContainersResponse\x12\x46\n\ncontainers\x18\x01 \x03(\x0b\x32,.containerd.services.containers.v1.ContainerB\x04\xc8\xde\x1f\x00\"_\n\x16\x43reateContainerRequest\x12\x45\n\tcontainer\x18\x01 \x01(\x0b\x32,.containerd.services.containers.v1.ContainerB\x04\xc8\xde\x1f\x00\"`\n\x17\x43reateContainerResponse\x12\x45\n\tcontainer\x18\x01 \x01(\x0b\x32,.containerd.services.containers.v1.ContainerB\x04\xc8\xde\x1f\x00\"\x90\x01\n\x16UpdateContainerRequest\x12\x45\n\tcontainer\x18\x01 \x01(\x0b\x32,.containerd.services.containers.v1.ContainerB\x04\xc8\xde\x1f\x00\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"`\n\x17UpdateContainerResponse\x12\x45\n\tcontainer\x18\x01 \x01(\x0b\x32,.containerd.services.containers.v1.ContainerB\x04\xc8\xde\x1f\x00\"$\n\x16\x44\x65leteContainerRequest\x12\n\n\x02id\x18\x01 \x01(\t\"W\n\x14ListContainerMessage\x12?\n\tcontainer\x18\x01 \x01(\x0b\x32,.containerd.services.containers.v1.Container2\xe4\x05\n\nContainers\x12v\n\x03Get\x12\x36.containerd.services.containers.v1.GetContainerRequest\x1a\x37.containerd.services.containers.v1.GetContainerResponse\x12{\n\x04List\x12\x38.containerd.services.containers.v1.ListContainersRequest\x1a\x39.containerd.services.containers.v1.ListContainersResponse\x12\x81\x01\n\nListStream\x12\x38.containerd.services.containers.v1.ListContainersRequest\x1a\x37.containerd.services.containers.v1.ListContainerMessage0\x01\x12\x7f\n\x06\x43reate\x12\x39.containerd.services.containers.v1.CreateContainerRequest\x1a:.containerd.services.containers.v1.CreateContainerResponse\x12\x7f\n\x06Update\x12\x39.containerd.services.containers.v1.UpdateContainerRequest\x1a:.containerd.services.containers.v1.UpdateContainerResponse\x12[\n\x06\x44\x65lete\x12\x39.containerd.services.containers.v1.DeleteContainerRequest\x1a\x16.google.protobuf.EmptyBHZFgithub.com/containerd/containerd/api/services/containers/v1;containersX\x00\x62\x06proto3'
  ,
  dependencies=[containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CONTAINER_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='containerd.services.containers.v1.Container.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.services.containers.v1.Container.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.services.containers.v1.Container.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=721,
  serialized_end=766,
)

_CONTAINER_RUNTIME = _descriptor.Descriptor(
  name='Runtime',
  full_name='containerd.services.containers.v1.Container.Runtime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='containerd.services.containers.v1.Container.Runtime.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='options', full_name='containerd.services.containers.v1.Container.Runtime.options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=768,
  serialized_end=830,
)

_CONTAINER_EXTENSIONSENTRY = _descriptor.Descriptor(
  name='ExtensionsEntry',
  full_name='containerd.services.containers.v1.Container.ExtensionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.services.containers.v1.Container.ExtensionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.services.containers.v1.Container.ExtensionsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=832,
  serialized_end=903,
)

_CONTAINER = _descriptor.Descriptor(
  name='Container',
  full_name='containerd.services.containers.v1.Container',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.services.containers.v1.Container.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='containerd.services.containers.v1.Container.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='containerd.services.containers.v1.Container.image', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='runtime', full_name='containerd.services.containers.v1.Container.runtime', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spec', full_name='containerd.services.containers.v1.Container.spec', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snapshotter', full_name='containerd.services.containers.v1.Container.snapshotter', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snapshot_key', full_name='containerd.services.containers.v1.Container.snapshot_key', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='containerd.services.containers.v1.Container.created_at', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\337\037\001\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='containerd.services.containers.v1.Container.updated_at', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\337\037\001\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extensions', full_name='containerd.services.containers.v1.Container.extensions', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONTAINER_LABELSENTRY, _CONTAINER_RUNTIME, _CONTAINER_EXTENSIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=903,
)


_GETCONTAINERREQUEST = _descriptor.Descriptor(
  name='GetContainerRequest',
  full_name='containerd.services.containers.v1.GetContainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.services.containers.v1.GetContainerRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=905,
  serialized_end=938,
)


_GETCONTAINERRESPONSE = _descriptor.Descriptor(
  name='GetContainerResponse',
  full_name='containerd.services.containers.v1.GetContainerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='container', full_name='containerd.services.containers.v1.GetContainerResponse.container', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=940,
  serialized_end=1033,
)


_LISTCONTAINERSREQUEST = _descriptor.Descriptor(
  name='ListContainersRequest',
  full_name='containerd.services.containers.v1.ListContainersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filters', full_name='containerd.services.containers.v1.ListContainersRequest.filters', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1035,
  serialized_end=1075,
)


_LISTCONTAINERSRESPONSE = _descriptor.Descriptor(
  name='ListContainersResponse',
  full_name='containerd.services.containers.v1.ListContainersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='containers', full_name='containerd.services.containers.v1.ListContainersResponse.containers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1077,
  serialized_end=1173,
)


_CREATECONTAINERREQUEST = _descriptor.Descriptor(
  name='CreateContainerRequest',
  full_name='containerd.services.containers.v1.CreateContainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='container', full_name='containerd.services.containers.v1.CreateContainerRequest.container', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1175,
  serialized_end=1270,
)


_CREATECONTAINERRESPONSE = _descriptor.Descriptor(
  name='CreateContainerResponse',
  full_name='containerd.services.containers.v1.CreateContainerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='container', full_name='containerd.services.containers.v1.CreateContainerResponse.container', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1272,
  serialized_end=1368,
)


_UPDATECONTAINERREQUEST = _descriptor.Descriptor(
  name='UpdateContainerRequest',
  full_name='containerd.services.containers.v1.UpdateContainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='container', full_name='containerd.services.containers.v1.UpdateContainerRequest.container', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='containerd.services.containers.v1.UpdateContainerRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1371,
  serialized_end=1515,
)


_UPDATECONTAINERRESPONSE = _descriptor.Descriptor(
  name='UpdateContainerResponse',
  full_name='containerd.services.containers.v1.UpdateContainerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='container', full_name='containerd.services.containers.v1.UpdateContainerResponse.container', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1517,
  serialized_end=1613,
)


_DELETECONTAINERREQUEST = _descriptor.Descriptor(
  name='DeleteContainerRequest',
  full_name='containerd.services.containers.v1.DeleteContainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.services.containers.v1.DeleteContainerRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1615,
  serialized_end=1651,
)


_LISTCONTAINERMESSAGE = _descriptor.Descriptor(
  name='ListContainerMessage',
  full_name='containerd.services.containers.v1.ListContainerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='container', full_name='containerd.services.containers.v1.ListContainerMessage.container', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1653,
  serialized_end=1740,
)

_CONTAINER_LABELSENTRY.containing_type = _CONTAINER
_CONTAINER_RUNTIME.fields_by_name['options'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONTAINER_RUNTIME.containing_type = _CONTAINER
_CONTAINER_EXTENSIONSENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONTAINER_EXTENSIONSENTRY.containing_type = _CONTAINER
_CONTAINER.fields_by_name['labels'].message_type = _CONTAINER_LABELSENTRY
_CONTAINER.fields_by_name['runtime'].message_type = _CONTAINER_RUNTIME
_CONTAINER.fields_by_name['spec'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONTAINER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONTAINER.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONTAINER.fields_by_name['extensions'].message_type = _CONTAINER_EXTENSIONSENTRY
_GETCONTAINERRESPONSE.fields_by_name['container'].message_type = _CONTAINER
_LISTCONTAINERSRESPONSE.fields_by_name['containers'].message_type = _CONTAINER
_CREATECONTAINERREQUEST.fields_by_name['container'].message_type = _CONTAINER
_CREATECONTAINERRESPONSE.fields_by_name['container'].message_type = _CONTAINER
_UPDATECONTAINERREQUEST.fields_by_name['container'].message_type = _CONTAINER
_UPDATECONTAINERREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATECONTAINERRESPONSE.fields_by_name['container'].message_type = _CONTAINER
_LISTCONTAINERMESSAGE.fields_by_name['container'].message_type = _CONTAINER
DESCRIPTOR.message_types_by_name['Container'] = _CONTAINER
DESCRIPTOR.message_types_by_name['GetContainerRequest'] = _GETCONTAINERREQUEST
DESCRIPTOR.message_types_by_name['GetContainerResponse'] = _GETCONTAINERRESPONSE
DESCRIPTOR.message_types_by_name['ListContainersRequest'] = _LISTCONTAINERSREQUEST
DESCRIPTOR.message_types_by_name['ListContainersResponse'] = _LISTCONTAINERSRESPONSE
DESCRIPTOR.message_types_by_name['CreateContainerRequest'] = _CREATECONTAINERREQUEST
DESCRIPTOR.message_types_by_name['CreateContainerResponse'] = _CREATECONTAINERRESPONSE
DESCRIPTOR.message_types_by_name['UpdateContainerRequest'] = _UPDATECONTAINERREQUEST
DESCRIPTOR.message_types_by_name['UpdateContainerResponse'] = _UPDATECONTAINERRESPONSE
DESCRIPTOR.message_types_by_name['DeleteContainerRequest'] = _DELETECONTAINERREQUEST
DESCRIPTOR.message_types_by_name['ListContainerMessage'] = _LISTCONTAINERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Container = _reflection.GeneratedProtocolMessageType('Container', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINER_LABELSENTRY,
    '__module__' : 'containerd.services.containers.v1.containers_pb2'
    # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.Container.LabelsEntry)
    })
  ,

  'Runtime' : _reflection.GeneratedProtocolMessageType('Runtime', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINER_RUNTIME,
    '__module__' : 'containerd.services.containers.v1.containers_pb2'
    # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.Container.Runtime)
    })
  ,

  'ExtensionsEntry' : _reflection.GeneratedProtocolMessageType('ExtensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINER_EXTENSIONSENTRY,
    '__module__' : 'containerd.services.containers.v1.containers_pb2'
    # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.Container.ExtensionsEntry)
    })
  ,
  'DESCRIPTOR' : _CONTAINER,
  '__module__' : 'containerd.services.containers.v1.containers_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.Container)
  })
_sym_db.RegisterMessage(Container)
_sym_db.RegisterMessage(Container.LabelsEntry)
_sym_db.RegisterMessage(Container.Runtime)
_sym_db.RegisterMessage(Container.ExtensionsEntry)

GetContainerRequest = _reflection.GeneratedProtocolMessageType('GetContainerRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONTAINERREQUEST,
  '__module__' : 'containerd.services.containers.v1.containers_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.GetContainerRequest)
  })
_sym_db.RegisterMessage(GetContainerRequest)

GetContainerResponse = _reflection.GeneratedProtocolMessageType('GetContainerResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCONTAINERRESPONSE,
  '__module__' : 'containerd.services.containers.v1.containers_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.GetContainerResponse)
  })
_sym_db.RegisterMessage(GetContainerResponse)

ListContainersRequest = _reflection.GeneratedProtocolMessageType('ListContainersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONTAINERSREQUEST,
  '__module__' : 'containerd.services.containers.v1.containers_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.ListContainersRequest)
  })
_sym_db.RegisterMessage(ListContainersRequest)

ListContainersResponse = _reflection.GeneratedProtocolMessageType('ListContainersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONTAINERSRESPONSE,
  '__module__' : 'containerd.services.containers.v1.containers_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.ListContainersResponse)
  })
_sym_db.RegisterMessage(ListContainersResponse)

CreateContainerRequest = _reflection.GeneratedProtocolMessageType('CreateContainerRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONTAINERREQUEST,
  '__module__' : 'containerd.services.containers.v1.containers_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.CreateContainerRequest)
  })
_sym_db.RegisterMessage(CreateContainerRequest)

CreateContainerResponse = _reflection.GeneratedProtocolMessageType('CreateContainerResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONTAINERRESPONSE,
  '__module__' : 'containerd.services.containers.v1.containers_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.CreateContainerResponse)
  })
_sym_db.RegisterMessage(CreateContainerResponse)

UpdateContainerRequest = _reflection.GeneratedProtocolMessageType('UpdateContainerRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONTAINERREQUEST,
  '__module__' : 'containerd.services.containers.v1.containers_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.UpdateContainerRequest)
  })
_sym_db.RegisterMessage(UpdateContainerRequest)

UpdateContainerResponse = _reflection.GeneratedProtocolMessageType('UpdateContainerResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONTAINERRESPONSE,
  '__module__' : 'containerd.services.containers.v1.containers_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.UpdateContainerResponse)
  })
_sym_db.RegisterMessage(UpdateContainerResponse)

DeleteContainerRequest = _reflection.GeneratedProtocolMessageType('DeleteContainerRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECONTAINERREQUEST,
  '__module__' : 'containerd.services.containers.v1.containers_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.DeleteContainerRequest)
  })
_sym_db.RegisterMessage(DeleteContainerRequest)

ListContainerMessage = _reflection.GeneratedProtocolMessageType('ListContainerMessage', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONTAINERMESSAGE,
  '__module__' : 'containerd.services.containers.v1.containers_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.containers.v1.ListContainerMessage)
  })
_sym_db.RegisterMessage(ListContainerMessage)


DESCRIPTOR._options = None
_CONTAINER_LABELSENTRY._options = None
_CONTAINER_EXTENSIONSENTRY._options = None
_CONTAINER.fields_by_name['created_at']._options = None
_CONTAINER.fields_by_name['updated_at']._options = None
_CONTAINER.fields_by_name['extensions']._options = None
_GETCONTAINERRESPONSE.fields_by_name['container']._options = None
_LISTCONTAINERSRESPONSE.fields_by_name['containers']._options = None
_CREATECONTAINERREQUEST.fields_by_name['container']._options = None
_CREATECONTAINERRESPONSE.fields_by_name['container']._options = None
_UPDATECONTAINERREQUEST.fields_by_name['container']._options = None
_UPDATECONTAINERRESPONSE.fields_by_name['container']._options = None

_CONTAINERS = _descriptor.ServiceDescriptor(
  name='Containers',
  full_name='containerd.services.containers.v1.Containers',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1743,
  serialized_end=2483,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='containerd.services.containers.v1.Containers.Get',
    index=0,
    containing_service=None,
    input_type=_GETCONTAINERREQUEST,
    output_type=_GETCONTAINERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='containerd.services.containers.v1.Containers.List',
    index=1,
    containing_service=None,
    input_type=_LISTCONTAINERSREQUEST,
    output_type=_LISTCONTAINERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListStream',
    full_name='containerd.services.containers.v1.Containers.ListStream',
    index=2,
    containing_service=None,
    input_type=_LISTCONTAINERSREQUEST,
    output_type=_LISTCONTAINERMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='containerd.services.containers.v1.Containers.Create',
    index=3,
    containing_service=None,
    input_type=_CREATECONTAINERREQUEST,
    output_type=_CREATECONTAINERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='containerd.services.containers.v1.Containers.Update',
    index=4,
    containing_service=None,
    input_type=_UPDATECONTAINERREQUEST,
    output_type=_UPDATECONTAINERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='containerd.services.containers.v1.Containers.Delete',
    index=5,
    containing_service=None,
    input_type=_DELETECONTAINERREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTAINERS)

DESCRIPTOR.services_by_name['Containers'] = _CONTAINERS

# @@protoc_insertion_point(module_scope)
