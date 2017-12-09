from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = 'jwc_user'

    student_ID = Column(String(13), primary_key=True) # pk
    # NOTE: user 增加了wx_id 字段
    wx_ID = Column(String(32))
    jwc_passwd = Column(String(20))
    course_schedule = relationship(
        "UserCourseSchedule",
        backref='User',
        lazy='dynamic'
    )


    def __repr__(self):
        return '<user {}>'.format(self.student_ID)

class Course(Base):

    __tablename__ = 'jwc_course'
    ID = Column(String(40), primary_key=True)
    course_number = Column(String(9)) # pk
    course_serial_number = Column(String(2))
    offering_date = Column(String(100))
    course_name = Column(String(100))
    training_program = Column(String(100))
    course_credit = Column(String(4))
    course_type = Column(String(4))
    exam_type = Column(String(50))
    teacher = Column(String(100))
    offering_weeks = Column(String(100))
    offering_day_of_week = Column(String(100))
    class_section = Column(String(100))
    campus = Column(String(100))
    teaching_building = Column(String(100))
    classroom = Column(String(100))

    user_course_schedule = relationship(
        "UserCourseSchedule",
        backref='Course',
        lazy='dynamic'
    )

    def __repr__(self):
        return '<课程 {}>'.format(self.course_number)

class UserCourseSchedule(Base):
    __tablename__ = 'jwc_user_course_schedule'

    student_ID = Column(
        String(13),
        ForeignKey('jwc_user.student_ID', ondelete='CASCADE'),
        primary_key=True
    )

    course_ID = Column(
        String(40),
        ForeignKey('jwc_course.ID', ondelete='CASCADE'),
        primary_key=True
    )

    study_mode = Column(String(8))
    course_selection_state = Column(String(8))

    def __repr__(self):
        return '<{} 选课 {}>'.format(self.student_ID, self.course_ID)

class Task(Base):
    __tablename__ = 'jwc_task'
    task_ID = Column(String(40), primary_key=True)
    task = Column(Text())
    thour = Column(String(2))
    tmin = Column(String(2))
    tyear = Column(String(4))
    tmonth = Column(String(2))
    tday = Column(String(2))