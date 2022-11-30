from flask import Blueprint

home = Blueprint('home', __name__)

@home.get("/")
def index():
    try:
        return {"hello": "world"}
    except Exception as e:
        raise e