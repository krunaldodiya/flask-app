from app.models.employee import Employee
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class EmployeeSchema(SQLAlchemySchema):
  class Meta:
    model = Employee
    include_relationships = True
    load_instance = True
  
  id = auto_field()
  name = auto_field()
  age = auto_field()
  company_id = auto_field()
  created_at = auto_field()
  updated_at = auto_field()
