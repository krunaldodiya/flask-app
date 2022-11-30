from app.config.fyers import config
from app.middlewares.login_required import login_required
from flask import Blueprint

import requests

user = Blueprint('user', __name__)

@user.get("/user/<int:user_id>")
@login_required
def profile(user_id, user):
    try:
        return {'user_id': user_id, 'user': user}
    except Exception as e:
        raise e

@user.post("/user/algo/<type>")
@login_required
def run_algo(type, user):
    try:
        send = requests.post(url="http://localhost:4000/containers", data={
            'type': type,
            'session_id': user.id,
            'config': config
        })

        return {'user_id': type, 'user': user}
    except Exception as e:
        raise e
