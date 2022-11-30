from app.schemas.company import CompanySchema
from app.schemas.employee import EmployeeSchema
from marshmallow import fields


class GetEmployeeByIdResponse(EmployeeSchema):
  company = fields.Nested(CompanySchema)

class GetAllEmployeesResponse(EmployeeSchema):
  company = fields.Nested(CompanySchema)

class CreateEmployeeResponse(EmployeeSchema):
  company = fields.Nested(CompanySchema)
