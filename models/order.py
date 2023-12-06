#!/usr/bin/env python3

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Float


class Order(BaseModel, Base):
    __tablename__ = 'orders'

    price = Column(Float(), nullable=False, default=0.0)
