from typing import List

from ..project.injectors import DB
from .models import Job, User
from .schemas import JobSchema, UserSchema

session = DB.instance().session


class JobService:
    @staticmethod
    def get_all():
        return session.query(Job).all()

    @staticmethod
    def create(new_job_link: str) -> bool:
        """
        Creates new Job instance from dictionary
        :param new_job_link: string for JobSchema
        :return: is the Job instance new in db or existing
        """
        new_job = dict(link=new_job_link)
        job = Job(**JobSchema().load(new_job))

        ex_job = session.query(Job).filter(Job.link == new_job["link"]).first()
        if ex_job:
            return False
        else:
            session.add(job)
            session.commit()
            return True


class UserService:
    @staticmethod
    def get_all_ids() -> List[int]:
        users = session.query(User).all()
        ids: List[int] = [user.chat_id for user in users]
        return ids

    @staticmethod
    def create(new_user_chat_id: int) -> bool:
        """
        Creates new Job instance from dictionary
        :param new_user_chat_id: id of chat by telebot
        :return: is the Job instance new in db or existing
        """
        new_user = dict(chat_id=new_user_chat_id)
        usr = User(**UserSchema().load(new_user))
        print(id(DB.instance()))
        ex_usr = session.query(User).filter(User.chat_id == new_user["chat_id"]).first()
        if ex_usr:
            return False
        else:
            session.add(usr)
            session.commit()
            return True
