from ..project.injectors import DB
from sqlalchemy import Column, Integer, String, Text, Date
Base = DB.instance().Base


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    link = Column(String(250), unique=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    company = Column(String(40), nullable=False)
    date = Column(Date)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique=True, nullable=False)
