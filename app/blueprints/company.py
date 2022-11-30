from app.models.company import Company
from app.schemas.requests.company import CreateCompanyRequest
from app.schemas.responses.company import (CreateCompanyResponse,
                                           GetAllCompaniesResponse,
                                           GetCompanyByIdResponse,
                                           GetEmployeesByCompanyIdResponse)
from flask import Blueprint, request
from setup import db

company = Blueprint('company', __name__)

@company.get("/companies")
def get_all_companies():
    try:
        companies = Company.query.all()

        return GetAllCompaniesResponse(many=True).dump(companies)
    except Exception as e:
        raise e


@company.get("/companies/<int:company_id>")
def get_company_by_id(company_id):
    try:
        company = Company.query.filter_by(id=company_id).first()

        if not company:
            return {"errors": f"Company with id {company_id} does not exist"}

        return GetCompanyByIdResponse().dump(company)
    except Exception as e:
        raise e


@company.post("/companies")
def create_company():
    try:
        payload = request.json

        errors = CreateCompanyRequest().validate(payload)

        if errors:
            return {'errors': errors}
        
        company = Company(name=payload['name'])

        db.session.add(company)
        db.session.commit()
        db.session.refresh(company)

        return CreateCompanyResponse().dump(company)
    except Exception as e:
        raise e


@company.delete("/companies/<int:company_id>")
def delete_company_by_id(company_id):
    try:
        company = Company.query.filter_by(id=company_id).first()

        if not company:
            return {"errors": f"Company with id {company_id} does not exist"}

        db.session.delete(company)
        db.session.commit()

        return {'message': f"Company with id {company_id} deleted"}
    except Exception as e:
        raise e


@company.get("/companies/<int:company_id>/employees")
def get_employees_by_company_id(company_id):
    try:
        company = Company.query.filter_by(id=company_id).first()

        if not company:
            return {"errors": f"Company with id {company_id} does not exist"}

        return GetEmployeesByCompanyIdResponse().dump(company)
    except Exception as e:
        raise e
