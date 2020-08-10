class DB:
    """Singleton for db init"""
    __db = None

    class WrappedDB:
        """Wrapped database engine class"""

        def __init__(self, url: str):
            from sqlalchemy import create_engine
            self.__engine = create_engine(url, echo=True)

        @property
        def engine(self):
            return self.__engine

    @staticmethod
    def instance(*args) -> WrappedDB:
        if not DB.__db:
            DB.__db = DB.WrappedDB(*args)

        return DB.__db

    def __init__(self):
        """Constructor not implemented in singleton pattern"""
        raise NotImplementedError()

