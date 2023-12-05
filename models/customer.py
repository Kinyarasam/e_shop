#!/usr/bin/env python3

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Customer(BaseModel, Base):
    __tablename__ = 'customer'

    first_name = Column(String(128))
    email = Column(String(128))
