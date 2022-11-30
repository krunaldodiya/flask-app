from setup import db
from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from sqlalchemy.orm import relationship


class Company(db.Model):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    employees = relationship("Employee", back_populates="company")