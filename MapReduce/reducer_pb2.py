# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reducer.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rreducer.proto\x12\x07reducer\"#\n\x0cReduceRequst\x12\x13\n\x0b\x63\x65ntroid_id\x18\x01 \x01(\x05\"E\n\x0eReduceResponse\x12\x13\n\x0b\x63\x65ntroid_id\x18\x01 \x01(\x05\x12\x1e\n\x06points\x18\x02 \x03(\x0b\x32\x0e.reducer.Point\"\x18\n\x05Point\x12\x0f\n\x07\x64im_val\x18\x01 \x03(\x02\x32\x43\n\x07Reducer\x12\x38\n\x06Reduce\x12\x15.reducer.ReduceRequst\x1a\x17.reducer.ReduceResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reducer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REDUCEREQUST']._serialized_start=26
  _globals['_REDUCEREQUST']._serialized_end=61
  _globals['_REDUCERESPONSE']._serialized_start=63
  _globals['_REDUCERESPONSE']._serialized_end=132
  _globals['_POINT']._serialized_start=134
  _globals['_POINT']._serialized_end=158
  _globals['_REDUCER']._serialized_start=160
  _globals['_REDUCER']._serialized_end=227
# @@protoc_insertion_point(module_scope)
