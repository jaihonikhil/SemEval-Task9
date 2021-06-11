# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tapas/protos/interaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tapas/protos/interaction.proto',
  package='language.tapas',
  syntax='proto2',
  serialized_pb=_b('\n\x1etapas/protos/interaction.proto\x12\x0elanguage.tapas\"w\n\x0bInteraction\x12\n\n\x02id\x18\x01 \x01(\t\x12$\n\x05table\x18\x02 \x01(\x0b\x32\x15.language.tapas.Table\x12+\n\tquestions\x18\x03 \x03(\x0b\x32\x18.language.tapas.Question*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"\xdb\x01\n\x08Question\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x15\n\roriginal_text\x18\x03 \x01(\t\x12\x36\n\x0b\x61nnotations\x18\x04 \x01(\x0b\x32!.language.tapas.NumericValueSpans\x12&\n\x06\x61nswer\x18\x05 \x01(\x0b\x32\x16.language.tapas.Answer\x12\x33\n\x13\x61lternative_answers\x18\x06 \x03(\x0b\x32\x16.language.tapas.Answer*\t\x08\x90N\x10\x80\x80\x80\x80\x02\";\n\x10\x41nswerCoordinate\x12\x11\n\trow_index\x18\x01 \x01(\x05\x12\x14\n\x0c\x63olumn_index\x18\x02 \x01(\x05\"\xb5\x02\n\x06\x41nswer\x12<\n\x12\x61nswer_coordinates\x18\x01 \x03(\x0b\x32 .language.tapas.AnswerCoordinate\x12H\n\x14\x61ggregation_function\x18\x02 \x01(\x0e\x32*.language.tapas.Answer.AggregationFunction\x12\x14\n\x0c\x61nswer_texts\x18\x03 \x03(\t\x12\x13\n\x0b\x66loat_value\x18\x04 \x01(\x02\x12\x16\n\x08is_valid\x18\x05 \x01(\x08:\x04true\x12\x13\n\x0b\x63lass_index\x18\x06 \x01(\x05\"@\n\x13\x41ggregationFunction\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03SUM\x10\x01\x12\x0b\n\x07\x41VERAGE\x10\x02\x12\t\n\x05\x43OUNT\x10\x03*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"\xf1\x01\n\x05Table\x12%\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x14.language.tapas.Cell\x12#\n\x04rows\x18\x02 \x03(\x0b\x32\x15.language.tapas.Cells\x12\x10\n\x08table_id\x18\x03 \x01(\t\x12\x16\n\x0e\x64ocument_title\x18\x04 \x01(\t\x12\x0f\n\x07\x63\x61ption\x18\x05 \x01(\t\x12\x14\n\x0c\x64ocument_url\x18\x06 \x01(\t\x12!\n\x19\x61lternative_document_urls\x18\x07 \x03(\t\x12\x1d\n\x15\x61lternative_table_ids\x18\x08 \x03(\t*\t\x08\x90N\x10\x80\x80\x80\x80\x02\"T\n\x04\x43\x65ll\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x33\n\rnumeric_value\x18\x02 \x01(\x0b\x32\x1c.language.tapas.NumericValue*\t\x08\x90N\x10\x80\x80\x80\x80\x02\",\n\x05\x43\x65lls\x12#\n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32\x14.language.tapas.Cell\"0\n\x04\x44\x61te\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x05\"T\n\x0cNumericValue\x12\x15\n\x0b\x66loat_value\x18\x01 \x01(\x02H\x00\x12$\n\x04\x64\x61te\x18\x02 \x01(\x0b\x32\x14.language.tapas.DateH\x00\x42\x07\n\x05value\"h\n\x10NumericValueSpan\x12\x13\n\x0b\x62\x65gin_index\x18\x01 \x01(\x05\x12\x11\n\tend_index\x18\x02 \x01(\x05\x12,\n\x06values\x18\x03 \x03(\x0b\x32\x1c.language.tapas.NumericValue\"D\n\x11NumericValueSpans\x12/\n\x05spans\x18\x01 \x03(\x0b\x32 .language.tapas.NumericValueSpan')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ANSWER_AGGREGATIONFUNCTION = _descriptor.EnumDescriptor(
  name='AggregationFunction',
  full_name='language.tapas.Answer.AggregationFunction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVERAGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUNT', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=689,
  serialized_end=753,
)
_sym_db.RegisterEnumDescriptor(_ANSWER_AGGREGATIONFUNCTION)


_INTERACTION = _descriptor.Descriptor(
  name='Interaction',
  full_name='language.tapas.Interaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='language.tapas.Interaction.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table', full_name='language.tapas.Interaction.table', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='questions', full_name='language.tapas.Interaction.questions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(10000, 536870912), ],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=169,
)


_QUESTION = _descriptor.Descriptor(
  name='Question',
  full_name='language.tapas.Question',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='language.tapas.Question.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='language.tapas.Question.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='original_text', full_name='language.tapas.Question.original_text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='language.tapas.Question.annotations', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer', full_name='language.tapas.Question.answer', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternative_answers', full_name='language.tapas.Question.alternative_answers', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(10000, 536870912), ],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=391,
)


_ANSWERCOORDINATE = _descriptor.Descriptor(
  name='AnswerCoordinate',
  full_name='language.tapas.AnswerCoordinate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_index', full_name='language.tapas.AnswerCoordinate.row_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='column_index', full_name='language.tapas.AnswerCoordinate.column_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=393,
  serialized_end=452,
)


_ANSWER = _descriptor.Descriptor(
  name='Answer',
  full_name='language.tapas.Answer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer_coordinates', full_name='language.tapas.Answer.answer_coordinates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aggregation_function', full_name='language.tapas.Answer.aggregation_function', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer_texts', full_name='language.tapas.Answer.answer_texts', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='language.tapas.Answer.float_value', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_valid', full_name='language.tapas.Answer.is_valid', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_index', full_name='language.tapas.Answer.class_index', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ANSWER_AGGREGATIONFUNCTION,
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(10000, 536870912), ],
  oneofs=[
  ],
  serialized_start=455,
  serialized_end=764,
)


_TABLE = _descriptor.Descriptor(
  name='Table',
  full_name='language.tapas.Table',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='language.tapas.Table.columns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rows', full_name='language.tapas.Table.rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table_id', full_name='language.tapas.Table.table_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='document_title', full_name='language.tapas.Table.document_title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caption', full_name='language.tapas.Table.caption', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='document_url', full_name='language.tapas.Table.document_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternative_document_urls', full_name='language.tapas.Table.alternative_document_urls', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternative_table_ids', full_name='language.tapas.Table.alternative_table_ids', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(10000, 536870912), ],
  oneofs=[
  ],
  serialized_start=767,
  serialized_end=1008,
)


_CELL = _descriptor.Descriptor(
  name='Cell',
  full_name='language.tapas.Cell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='language.tapas.Cell.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numeric_value', full_name='language.tapas.Cell.numeric_value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(10000, 536870912), ],
  oneofs=[
  ],
  serialized_start=1010,
  serialized_end=1094,
)


_CELLS = _descriptor.Descriptor(
  name='Cells',
  full_name='language.tapas.Cells',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='language.tapas.Cells.cells', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1096,
  serialized_end=1140,
)


_DATE = _descriptor.Descriptor(
  name='Date',
  full_name='language.tapas.Date',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='language.tapas.Date.year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='month', full_name='language.tapas.Date.month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='day', full_name='language.tapas.Date.day', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1142,
  serialized_end=1190,
)


_NUMERICVALUE = _descriptor.Descriptor(
  name='NumericValue',
  full_name='language.tapas.NumericValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='float_value', full_name='language.tapas.NumericValue.float_value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='language.tapas.NumericValue.date', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='language.tapas.NumericValue.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1192,
  serialized_end=1276,
)


_NUMERICVALUESPAN = _descriptor.Descriptor(
  name='NumericValueSpan',
  full_name='language.tapas.NumericValueSpan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='begin_index', full_name='language.tapas.NumericValueSpan.begin_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_index', full_name='language.tapas.NumericValueSpan.end_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='language.tapas.NumericValueSpan.values', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1278,
  serialized_end=1382,
)


_NUMERICVALUESPANS = _descriptor.Descriptor(
  name='NumericValueSpans',
  full_name='language.tapas.NumericValueSpans',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spans', full_name='language.tapas.NumericValueSpans.spans', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1384,
  serialized_end=1452,
)

_INTERACTION.fields_by_name['table'].message_type = _TABLE
_INTERACTION.fields_by_name['questions'].message_type = _QUESTION
_QUESTION.fields_by_name['annotations'].message_type = _NUMERICVALUESPANS
_QUESTION.fields_by_name['answer'].message_type = _ANSWER
_QUESTION.fields_by_name['alternative_answers'].message_type = _ANSWER
_ANSWER.fields_by_name['answer_coordinates'].message_type = _ANSWERCOORDINATE
_ANSWER.fields_by_name['aggregation_function'].enum_type = _ANSWER_AGGREGATIONFUNCTION
_ANSWER_AGGREGATIONFUNCTION.containing_type = _ANSWER
_TABLE.fields_by_name['columns'].message_type = _CELL
_TABLE.fields_by_name['rows'].message_type = _CELLS
_CELL.fields_by_name['numeric_value'].message_type = _NUMERICVALUE
_CELLS.fields_by_name['cells'].message_type = _CELL
_NUMERICVALUE.fields_by_name['date'].message_type = _DATE
_NUMERICVALUE.oneofs_by_name['value'].fields.append(
  _NUMERICVALUE.fields_by_name['float_value'])
_NUMERICVALUE.fields_by_name['float_value'].containing_oneof = _NUMERICVALUE.oneofs_by_name['value']
_NUMERICVALUE.oneofs_by_name['value'].fields.append(
  _NUMERICVALUE.fields_by_name['date'])
_NUMERICVALUE.fields_by_name['date'].containing_oneof = _NUMERICVALUE.oneofs_by_name['value']
_NUMERICVALUESPAN.fields_by_name['values'].message_type = _NUMERICVALUE
_NUMERICVALUESPANS.fields_by_name['spans'].message_type = _NUMERICVALUESPAN
DESCRIPTOR.message_types_by_name['Interaction'] = _INTERACTION
DESCRIPTOR.message_types_by_name['Question'] = _QUESTION
DESCRIPTOR.message_types_by_name['AnswerCoordinate'] = _ANSWERCOORDINATE
DESCRIPTOR.message_types_by_name['Answer'] = _ANSWER
DESCRIPTOR.message_types_by_name['Table'] = _TABLE
DESCRIPTOR.message_types_by_name['Cell'] = _CELL
DESCRIPTOR.message_types_by_name['Cells'] = _CELLS
DESCRIPTOR.message_types_by_name['Date'] = _DATE
DESCRIPTOR.message_types_by_name['NumericValue'] = _NUMERICVALUE
DESCRIPTOR.message_types_by_name['NumericValueSpan'] = _NUMERICVALUESPAN
DESCRIPTOR.message_types_by_name['NumericValueSpans'] = _NUMERICVALUESPANS

Interaction = _reflection.GeneratedProtocolMessageType('Interaction', (_message.Message,), dict(
  DESCRIPTOR = _INTERACTION,
  __module__ = 'tapas.protos.interaction_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.Interaction)
  ))
_sym_db.RegisterMessage(Interaction)

Question = _reflection.GeneratedProtocolMessageType('Question', (_message.Message,), dict(
  DESCRIPTOR = _QUESTION,
  __module__ = 'tapas.protos.interaction_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.Question)
  ))
_sym_db.RegisterMessage(Question)

AnswerCoordinate = _reflection.GeneratedProtocolMessageType('AnswerCoordinate', (_message.Message,), dict(
  DESCRIPTOR = _ANSWERCOORDINATE,
  __module__ = 'tapas.protos.interaction_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.AnswerCoordinate)
  ))
_sym_db.RegisterMessage(AnswerCoordinate)

Answer = _reflection.GeneratedProtocolMessageType('Answer', (_message.Message,), dict(
  DESCRIPTOR = _ANSWER,
  __module__ = 'tapas.protos.interaction_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.Answer)
  ))
_sym_db.RegisterMessage(Answer)

Table = _reflection.GeneratedProtocolMessageType('Table', (_message.Message,), dict(
  DESCRIPTOR = _TABLE,
  __module__ = 'tapas.protos.interaction_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.Table)
  ))
_sym_db.RegisterMessage(Table)

Cell = _reflection.GeneratedProtocolMessageType('Cell', (_message.Message,), dict(
  DESCRIPTOR = _CELL,
  __module__ = 'tapas.protos.interaction_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.Cell)
  ))
_sym_db.RegisterMessage(Cell)

Cells = _reflection.GeneratedProtocolMessageType('Cells', (_message.Message,), dict(
  DESCRIPTOR = _CELLS,
  __module__ = 'tapas.protos.interaction_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.Cells)
  ))
_sym_db.RegisterMessage(Cells)

Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), dict(
  DESCRIPTOR = _DATE,
  __module__ = 'tapas.protos.interaction_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.Date)
  ))
_sym_db.RegisterMessage(Date)

NumericValue = _reflection.GeneratedProtocolMessageType('NumericValue', (_message.Message,), dict(
  DESCRIPTOR = _NUMERICVALUE,
  __module__ = 'tapas.protos.interaction_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.NumericValue)
  ))
_sym_db.RegisterMessage(NumericValue)

NumericValueSpan = _reflection.GeneratedProtocolMessageType('NumericValueSpan', (_message.Message,), dict(
  DESCRIPTOR = _NUMERICVALUESPAN,
  __module__ = 'tapas.protos.interaction_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.NumericValueSpan)
  ))
_sym_db.RegisterMessage(NumericValueSpan)

NumericValueSpans = _reflection.GeneratedProtocolMessageType('NumericValueSpans', (_message.Message,), dict(
  DESCRIPTOR = _NUMERICVALUESPANS,
  __module__ = 'tapas.protos.interaction_pb2'
  # @@protoc_insertion_point(class_scope:language.tapas.NumericValueSpans)
  ))
_sym_db.RegisterMessage(NumericValueSpans)


# @@protoc_insertion_point(module_scope)
