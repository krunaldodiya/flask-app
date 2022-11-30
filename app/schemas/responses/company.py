from app.schemas.company import CompanySchema
from app.schemas.employee import EmployeeSchema
from marshmallow import fields


class GetEmployeesByCompanyIdResponse(CompanySchema):
  employees = fields.List(fields.Nested(EmployeeSchema))

class GetCompanyByIdResponse(CompanySchema):
  pass

class GetAllCompaniesResponse(CompanySchema):
  pass

class CreateCompanyResponse(CompanySchema):
  pass

