#!/usr/bin/env python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Address(BaseModel, Base):
    __tablename__ = 'address'

    city = Column(String(128))
    building = Column(String(128))
