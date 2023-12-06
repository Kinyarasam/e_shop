#!/usr/bin/env python3

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Customer(BaseModel, Base):
    __tablename__ = 'customers'

    first_name = Column(String(128))
    email = Column(String(128))
    addresses = relationship('Address', backref="customer",
                             cascade="all, delete, delete-orphan")
