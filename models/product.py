#!/usr/bin/env python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float


class Product(BaseModel, Base):
    __tablename__ = 'products'

    name = Column(String(512))
    product_type = Column(String(128))
    price = Column(Float, nullable=False, default=0.0)
    color = Column(String(60))
