import time
from typing import List
IMG_NAME = 'out.jpg'


class DB:
    """Singleton for db init"""
    __db = None

    class WrappedDB:
        """Wrapped database engine class"""

        def __init__(self, url: str):
            from sqlalchemy import create_engine
            from sqlalchemy.orm import sessionmaker
            from sqlalchemy.ext.declarative import declarative_base
            self.__Base = declarative_base()

            self.__engine = create_engine(url, echo=True)

            self.__session = sessionmaker(bind=self.__engine)()

        @property
        def engine(self):
            return self.__engine

        @property
        def Base(self):
            return self.__Base

        @property
        def session(self):
            return self.__session

        def init_db(self):
            self.__session.commit()
            self.__Base.metadata.drop_all(self.__engine)
            self.__Base.metadata.create_all(self.__engine)
            # self.__session.commit()

    @staticmethod
    def instance(*args) -> WrappedDB:
        if not DB.__db:
            DB.__db = DB.WrappedDB(*args)

        return DB.__db

    def __init__(self):
        """Constructor not implemented in singleton pattern"""
        raise NotImplementedError()


class Request:
    def __init__(self, users: List[int], text_message: str):
        self.__users = users
        self.__message = text_message
        self.image = IMG_NAME

    @property
    def users_id(self):
        return self.__users

    @property
    def message(self):
        return self.__message


def inf(func):
    def wrapper(*args):
        while True:
            try:
                return func(*args)
            except:
                print('Something goes wrong!!')
                time.sleep(10)
    return wrapper
