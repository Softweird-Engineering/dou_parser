from ..project.injectors import DB
from sqlalchemy import Column, Integer, String
Base = DB.instance().Base


class Job(Base):
    __tablename__ = 'jobs' # noqa

    id = Column(Integer, primary_key=True)
    link = Column(String(250), unique=True)


class User(Base):
    __tablename__ = 'users' # noqa

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique=True, nullable=False)
