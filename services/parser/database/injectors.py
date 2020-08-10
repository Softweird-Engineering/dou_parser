class DB:
    """Singleton for db init"""
    __db = None

    class WrappedDB:
        """Wrapped database engine class"""

        def __init__(self, url: str):
            from sqlalchemy import create_engine
            from sqlalchemy.orm import sessionmaker

            self.__engine = create_engine(url, echo=True)
            self.__session = sessionmaker(bind=self.__engine)

        @property
        def engine(self):
            return self.__engine

        @property
        def session(self):
            return self.__session

        def init_db(self):
            from .models import Base
            Base.metadata.create_all(self.__engine)
            self.__session.begin()

    @staticmethod
    def instance(*args) -> WrappedDB:
        if not DB.__db:
            DB.__db = DB.WrappedDB(*args)

        return DB.__db



    def __init__(self):
        """Constructor not implemented in singleton pattern"""
        raise NotImplementedError()

