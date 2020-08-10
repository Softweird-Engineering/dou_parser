from ..project.tests.fixtures import db
from datetime import datetime
from .services import JobService, Job, JobSchema


def test_get_all():
    j1 = Job(id=1, link='https://hangouts.google.com/call/yLTXfIKVHm08JPKDSs1QACE', date=datetime.now().date())