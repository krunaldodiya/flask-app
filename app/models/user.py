import jwt
from setup import db
from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, password):
        self.hash_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hash_password, password)

    @staticmethod
    def generate_token(user):
        return jwt.encode({"user": user}, "secret", algorithm="HS256")

    @staticmethod
    def verify_token(token):
        return jwt.decode(token, "secret", algorithms=['HS256'])

    @staticmethod
    def authenticate(user):
        token = User.generate_token(user)
        return {'user': user, 'token': token}
