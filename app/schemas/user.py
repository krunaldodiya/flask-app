from app.models.user import User
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class UserSchema(SQLAlchemySchema):
  class Meta:
    model = User
    include_relationships = True
    load_instance = True
  
  id = auto_field()
  name = auto_field()
  email = auto_field()
  created_at = auto_field()
  updated_at = auto_field()
