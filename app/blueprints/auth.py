from app.models.user import User
from app.schemas.requests.auth import LoginRequest, RegisterRequest
from app.schemas.user import UserSchema
from flask import Blueprint, request
from setup import db

auth = Blueprint('auth', __name__)

@auth.post("/login")
def login():
    try:
        payload = request.json

        errors = LoginRequest().validate(payload)

        if errors:
            return {'errors': errors}

        user = User.query.filter_by(email=payload['email']).first()

        if not user:
            return {'errors': "User not found"}

        valid_password = user.verify_password(payload['password'])

        if not valid_password:
            return {'errors': "Invalid password"}

        userSchema = UserSchema().dump(user)

        return User.authenticate(userSchema)
    except Exception as e:
        raise e

@auth.post("/register")
def register():
    try:
        payload = request.json

        errors = RegisterRequest().validate(payload)

        if errors:
            return {'errors': errors}

        exists = User.query.filter_by(email=payload['email']).first()

        if exists:
            return {'errors': "User already exists"}

        user = User(
            name=payload['name'], email=payload['email'], password=payload['password']
        )

        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

        userSchema = UserSchema().dump(user)

        return User.authenticate(userSchema)
    except Exception as e:
        raise e
