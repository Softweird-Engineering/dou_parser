from datetime import datetime
from ..tests.fixtures import db  # noqa
from .services import JobService, Job


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


# def test_create(db):
#     j1 = dict(link="https://hangouts.google.com/call/yLTXfIKVHm08JPKDSs1QACE", date=str(datetime.now().date()),
#               title='Sndfjsdnf', description="slidnojsdnfjksjndfksjdnfksjdnf", company="klsdfksndf")
#
#     res: bool = JobService.create(j1)
#
#     assert res
#     print(JobService.get_all())
#
#     j2 = dict(link="https://hangouts.google.com/call/yLTXfIKVHm08JPKDSs1QACE", date=str(datetime.now().date()),
#               title='Sndfjsdnf', description="slidnojsdnfjksjndfksjdnfksjdnf", company="klsdfksndf")
#
#     res2: bool = JobService.create(j2)
#
#     assert not res2
