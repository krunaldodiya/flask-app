from marshmallow import Schema, fields, validate


class LoginRequest(Schema):
  email = fields.Email(
    required=True,
  )

  password = fields.String(
    required=True,
    validate=[validate.Length(min=8)]
  )

class RegisterRequest(Schema):
  name = fields.String(
    required=True,
    validate=[validate.Length(min=3)]
  )

  email = fields.Email(
    required=True,
  )

  password = fields.String(
    required=True,
    validate=[validate.Length(min=8)]
  )
