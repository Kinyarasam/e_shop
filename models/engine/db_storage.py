#!/usr/bin/env python3
from models.base_model import Base
from models.customer import Customer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


DB_USERNAME = 'shop_dev'
DB_PASSWORD = 'shop_dev_pwd'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_DATABASE = 'shop_dev_db'
ENV = 'test'


CLASSES = {
    "Customer": Customer
}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self) -> None:
        connection_string = 'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'.format(
            username=DB_USERNAME,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_DATABASE
        )

        self.__engine = create_engine(connection_string)

        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        temp_dct = {}

        if cls is None:
            for c in CLASSES.values():
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = '{cl}.{id}'.format(
                        cl=obj.__class__.__name__, id=obj.id)
                    temp_dct[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = '{cl}.{id}'.format(cl=obj.__class__.__name__, id=obj.id)
                temp_dct[key] = obj

        return temp_dct

    def new(self, obj=None):
        if obj is None:
            return

        try:
            self.__session.add(obj)
            self.__session.flush()
            self.__session.refresh(obj)
        except Exception as e:
            self.__session.rollback()
            raise e

    def save(self):
        self.__session.commit()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory=session_factory)()
