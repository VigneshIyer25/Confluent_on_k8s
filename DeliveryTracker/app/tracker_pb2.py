# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tracker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rtracker.proto\x12\x07tracker\x1a\x1cgoogle/protobuf/struct.proto\"\x14\n\x12GetVehiclesRequest\",\n\x13GetVehiclesResponse\x12\x15\n\rvehicle_names\x18\x01 \x03(\t\"7\n\x1fStreamVehicleCoordinatesRequest\x12\x14\n\x0cvehicle_name\x18\x01 \x01(\t\"Q\n StreamVehicleCoordinatesResponse\x12-\n\rvehicleRecord\x18\x01 \x01(\x0b\x32\x16.tracker.VehicleRecord\"z\n\rVehicleRecord\x12\x12\n\ntruck_type\x18\x01 \x01(\t\x12\x14\n\x0ctruck_number\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12,\n\x0b\x63oordinates\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct2\xca\x01\n\x07Tracker\x12J\n\x0bGetVehicles\x12\x1b.tracker.GetVehiclesRequest\x1a\x1c.tracker.GetVehiclesResponse\"\x00\x12s\n\x18StreamVehicleCoordinates\x12(.tracker.StreamVehicleCoordinatesRequest\x1a).tracker.StreamVehicleCoordinatesResponse\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tracker_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_GETVEHICLESREQUEST']._serialized_start=56
  _globals['_GETVEHICLESREQUEST']._serialized_end=76
  _globals['_GETVEHICLESRESPONSE']._serialized_start=78
  _globals['_GETVEHICLESRESPONSE']._serialized_end=122
  _globals['_STREAMVEHICLECOORDINATESREQUEST']._serialized_start=124
  _globals['_STREAMVEHICLECOORDINATESREQUEST']._serialized_end=179
  _globals['_STREAMVEHICLECOORDINATESRESPONSE']._serialized_start=181
  _globals['_STREAMVEHICLECOORDINATESRESPONSE']._serialized_end=262
  _globals['_VEHICLERECORD']._serialized_start=264
  _globals['_VEHICLERECORD']._serialized_end=386
  _globals['_TRACKER']._serialized_start=389
  _globals['_TRACKER']._serialized_end=591
# @@protoc_insertion_point(module_scope)