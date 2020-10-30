from typing import List


class DSN:
    """Singleton for db init"""
    __dsn = None

    @staticmethod
    def get(name: str = ""):
        if not DSN.__dsn:
            DSN.__dsn = name

        return DSN.__dsn

    def __init__(self):
        """Constructor not implemented in singleton pattern"""
        raise NotImplementedError()


class Request:
    def __init__(self, users: List[int], text_message: str, img):
        self.__users = users
        self.__message = text_message
        self.image = img

    @property
    def users_id(self):
        return self.__users

    @property
    def message(self):
        return self.__message
