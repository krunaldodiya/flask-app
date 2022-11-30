from app.models.company import Company
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class CompanySchema(SQLAlchemySchema):
  class Meta:
    model = Company
    include_relationships = True
    load_instance = True
  
  id = auto_field()
  name = auto_field()
  created_at = auto_field()
  updated_at = auto_field()
