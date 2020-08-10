from ..project.tests.fixtures import db
from datetime import datetime
from .services import JobService, Job, JobSchema


def test_get_all(db):
    j1 = Job(link='https://hangouts.google.com/call/yLTXfIKVHm08JPKDSs1QACE', date=datetime.now().date(),
             title='Sndfjsdnf', description="slidnojsdnfjksjndfksjdnfksjdnf", company="klsdfksndf")
    j2 = Job(link='https://hangouts.google.com/call/yLTXfIKVHm08JPKDSs1sdff', date=datetime.now().date(),
             title='Sndfjsdnf', description="slidnojsdnfjksjndfksjdnfksjdnf", company="klsdfksndf")

    db.session.add(j1)
    db.session.add(j2)
    db.session.commit()

    result = JobService.get_all()

    assert j1 in result
    assert j2 in result
    assert len(result) == 2
