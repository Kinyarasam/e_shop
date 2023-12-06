#!/usr/bin/env python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean


class Address(BaseModel, Base):
    __tablename__ = 'addresses'

    city = Column(String(128))
    building = Column(String(128))
    customer_id = Column(String(60), ForeignKey(
        'customers.id'), nullable=False)
    default = Column(Boolean, nullable=False, default=False)
