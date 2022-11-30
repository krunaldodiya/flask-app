import os

from dotenv import load_dotenv

load_dotenv(".env")

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def import_blueprints():
  from app.blueprints.auth import auth
  from app.blueprints.company import company
  from app.blueprints.employee import employee
  from app.blueprints.fyers import fyers
  from app.blueprints.home import home
  from app.blueprints.user import user

  app.register_blueprint(home, url_prefix='/')
  app.register_blueprint(company, url_prefix='/')
  app.register_blueprint(employee, url_prefix='/')
  app.register_blueprint(fyers, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  app.register_blueprint(user, url_prefix='/')

def import_models():
  from app.models import company, employee, user

db = SQLAlchemy()

migrate = Migrate()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

db.init_app(app)

migrate.init_app(app, db)

import_models()

import_blueprints()

