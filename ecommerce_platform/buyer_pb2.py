# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buyer.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x62uyer.proto\x12\tecommerce\"4\n\x11\x42uyProductRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x0b\n\x03qty\x18\x02 \x01(\x05\"8\n\x12RateProductRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x0e\n\x06rating\x18\x02 \x01(\x05\"%\n\x13RateProductResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xa1\x01\n\x05\x42uyer\x12J\n\nBuyProduct\x12\x1c.ecommerce.BuyProductRequest\x1a\x1e.ecommerce.RateProductResponse\x12L\n\x0bRateProduct\x12\x1d.ecommerce.RateProductRequest\x1a\x1e.ecommerce.RateProductResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buyer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BUYPRODUCTREQUEST']._serialized_start=26
  _globals['_BUYPRODUCTREQUEST']._serialized_end=78
  _globals['_RATEPRODUCTREQUEST']._serialized_start=80
  _globals['_RATEPRODUCTREQUEST']._serialized_end=136
  _globals['_RATEPRODUCTRESPONSE']._serialized_start=138
  _globals['_RATEPRODUCTRESPONSE']._serialized_end=175
  _globals['_BUYER']._serialized_start=178
  _globals['_BUYER']._serialized_end=339
# @@protoc_insertion_point(module_scope)
