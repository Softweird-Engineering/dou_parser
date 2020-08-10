from ..project.injectors import DB
from .models import Job
from .schemas import JobSchema

session = DB.instance().session


class JobService:
    @staticmethod
    def get_all():
        return session.query(Job).all()

    @staticmethod
    def create(new_job: dict) -> bool:
        """
        Creates new Job instance from dictionary
        :param new_job: dictionary for JobSchema
        :return: is the Job instance new in db or existing
        """
        job = Job(**JobSchema().load(new_job))

        ex_job = session.query(Job).filter(Job.link == new_job["link"]).first()
        if ex_job:
            return False
        else:
            session.add(job)
            session.commit()
            return True

