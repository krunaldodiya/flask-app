from marshmallow import Schema, fields


class CreateCompanyRequest(Schema):
  name = fields.String(
    required=True,
  )
