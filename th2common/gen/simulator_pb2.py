#   Copyright 2020-2020 Exactpro (Exactpro Systems Limited)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: th2common/gen/simulator.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from th2common.gen import infra_pb2 as th2common_dot_gen_dot_infra__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='th2common/gen/simulator.proto',
  package='th2',
  syntax='proto3',
  serialized_options=b'\n\037com.exactpro.th2.simulator.grpcP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dth2common/gen/simulator.proto\x12\x03th2\x1a\x1bgoogle/protobuf/empty.proto\x1a\x19th2common/gen/infra.proto\"\x14\n\x06RuleID\x12\n\n\x02id\x18\x01 \x01(\x05\"a\n\x08RuleInfo\x12\x17\n\x02id\x18\x01 \x01(\x0b\x32\x0b.th2.RuleID\x12\x12\n\nclass_name\x18\x02 \x01(\t\x12(\n\rconnection_id\x18\x03 \x01(\x0b\x32\x11.th2.ConnectionID\"(\n\tRulesInfo\x12\x1b\n\x04info\x18\x01 \x03(\x0b\x32\r.th2.RuleInfo2\x81\x01\n\x10ServiceSimulator\x12\x33\n\nremoveRule\x12\x0b.th2.RuleID\x1a\x16.google.protobuf.Empty\"\x00\x12\x38\n\x0cgetRulesInfo\x12\x16.google.protobuf.Empty\x1a\x0e.th2.RulesInfo\"\x00\x42#\n\x1f\x63om.exactpro.th2.simulator.grpcP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,th2common_dot_gen_dot_infra__pb2.DESCRIPTOR,])




_RULEID = _descriptor.Descriptor(
  name='RuleID',
  full_name='th2.RuleID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='th2.RuleID.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=94,
  serialized_end=114,
)


_RULEINFO = _descriptor.Descriptor(
  name='RuleInfo',
  full_name='th2.RuleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='th2.RuleInfo.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='class_name', full_name='th2.RuleInfo.class_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='th2.RuleInfo.connection_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=116,
  serialized_end=213,
)


_RULESINFO = _descriptor.Descriptor(
  name='RulesInfo',
  full_name='th2.RulesInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='th2.RulesInfo.info', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=215,
  serialized_end=255,
)

_RULEINFO.fields_by_name['id'].message_type = _RULEID
_RULEINFO.fields_by_name['connection_id'].message_type = th2common_dot_gen_dot_infra__pb2._CONNECTIONID
_RULESINFO.fields_by_name['info'].message_type = _RULEINFO
DESCRIPTOR.message_types_by_name['RuleID'] = _RULEID
DESCRIPTOR.message_types_by_name['RuleInfo'] = _RULEINFO
DESCRIPTOR.message_types_by_name['RulesInfo'] = _RULESINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RuleID = _reflection.GeneratedProtocolMessageType('RuleID', (_message.Message,), {
  'DESCRIPTOR' : _RULEID,
  '__module__' : 'th2common.gen.simulator_pb2'
  # @@protoc_insertion_point(class_scope:th2.RuleID)
  })
_sym_db.RegisterMessage(RuleID)

RuleInfo = _reflection.GeneratedProtocolMessageType('RuleInfo', (_message.Message,), {
  'DESCRIPTOR' : _RULEINFO,
  '__module__' : 'th2common.gen.simulator_pb2'
  # @@protoc_insertion_point(class_scope:th2.RuleInfo)
  })
_sym_db.RegisterMessage(RuleInfo)

RulesInfo = _reflection.GeneratedProtocolMessageType('RulesInfo', (_message.Message,), {
  'DESCRIPTOR' : _RULESINFO,
  '__module__' : 'th2common.gen.simulator_pb2'
  # @@protoc_insertion_point(class_scope:th2.RulesInfo)
  })
_sym_db.RegisterMessage(RulesInfo)


DESCRIPTOR._options = None

_SERVICESIMULATOR = _descriptor.ServiceDescriptor(
  name='ServiceSimulator',
  full_name='th2.ServiceSimulator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=258,
  serialized_end=387,
  methods=[
  _descriptor.MethodDescriptor(
    name='removeRule',
    full_name='th2.ServiceSimulator.removeRule',
    index=0,
    containing_service=None,
    input_type=_RULEID,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getRulesInfo',
    full_name='th2.ServiceSimulator.getRulesInfo',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_RULESINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICESIMULATOR)

DESCRIPTOR.services_by_name['ServiceSimulator'] = _SERVICESIMULATOR

# @@protoc_insertion_point(module_scope)
