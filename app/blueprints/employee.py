from app.models.company import Company
from app.models.employee import Employee
from app.schemas.requests.employee import CreateEmployeeRequest
from app.schemas.responses.employee import (CreateEmployeeResponse,
                                            GetAllEmployeesResponse,
                                            GetEmployeeByIdResponse)
from flask import Blueprint, request
from setup import db

employee = Blueprint('employee', __name__)

@employee.get("/employees")
def get_all_employees():
    try:
        employees = Employee.query.all()

        return GetAllEmployeesResponse(many=True).dump(employees)
    except Exception as e:
        raise e


@employee.get("/employees/<int:employee_id>")
def get_employee_by_id(employee_id):
    try:
        employee = Employee.query.filter_by(id=employee_id).first()

        if not employee:
            return {"errors": f"Employee with id {employee_id} does not exist"}

        return GetEmployeeByIdResponse().dump(employee)
    except Exception as e:
        raise e

@employee.post("/companies/<int:company_id>/employees")
def add_employee(company_id):
    try:
        errors = CreateEmployeeRequest().validate(request.json)

        if errors:
            return {'errors': errors}

        company = Company.query.filter_by(id=company_id).first()

        if not company:
            return {"errors": f"Company with id {company_id} does not exist"}

        item = request.get_json()

        employee = Employee(name=item['name'], age=item['age'], company_id=company_id)

        db.session.add(employee)
        db.session.commit()
        db.session.refresh(employee)

        return CreateEmployeeResponse().dump(employee)
    except Exception as e:
        raise e


@employee.delete("/employees/<int:employee_id>")
def delete_employee_by_id(employee_id):
    try:
        employee = Employee.query.filter_by(id=employee_id).first()

        if not employee:
            return {"errors": f"Employee with id {employee_id} does not exist"}

        db.session.delete(employee)
        db.session.commit()

        return {'message': f"Employee with id {employee_id} deleted"}
    except Exception as e:
        raise e
