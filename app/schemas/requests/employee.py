from marshmallow import Schema, fields


class CreateEmployeeRequest(Schema):
  name = fields.String(
    required=True,
  )

  age = fields.Integer(
    required=True,
  )
