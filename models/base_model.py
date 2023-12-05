#!/usr/bin/env python3
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime


Base = declarative_base()


class BaseModel:
    id = Column(String(60), primary_key=True, unique=True,
                autoincrement=True, nullable=False, default=str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow())

    def __init__(self, *args, **kwargs) -> None:
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = datetime.datetime.utcnow()
        else:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    setattr(
                        self, k, datetime.datetime.fromisoformat(kwargs[k]))
                elif k != '__class__':
                    setattr(self, k, kwargs[k])

    def __str__(self) -> str:
        return '[{cls}] ({id}) {data}'.format(
            cls=self.__class__.__name__,
            id=self.id,
            data=self.__dict__
        )

    def save(self) -> None:
        self.updated_at = datetime.datetime.utcnow()

    def to_dict(self):
        temp_dct = dict(self.__dict__)
        temp_dct['__class__'] = self.__class__.__name__
        temp_dct['created_at'] = self.created_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        temp_dct['updated_at'] = self.updated_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')

        if '_sa_instances_state' in temp_dct.keys():
            del temp_dct['_sa_instances_state']

        return temp_dct
