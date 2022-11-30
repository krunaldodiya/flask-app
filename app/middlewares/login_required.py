from functools import wraps

import jwt
from flask import jsonify, make_response, request

from app.models.user import User


def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        prefix = 'Bearer '
        token = None
        # ensure the jwt-token is passed with the headers
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'][len(prefix):]

        if not token: # throw error if no token provided
            return make_response(jsonify({"message": "A valid token is missing!"}), 401)

        try:
            user = User.verify_token(token)

            return f(*args, **kwargs, user=user)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 401)

    return decorator
