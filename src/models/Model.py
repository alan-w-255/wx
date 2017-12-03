from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'jwc_user'
    student_ID = db.Column(db.String(12), primary_key=True) # pk
    jwc_passwd = db.Column(db.String(20))

    def __repr__(self):
        return '<user {}>'.format(self.student_ID)

class Course(db.Model):

    __tablename__ = 'jwc_course'
    course_number = db.Column(db.String(9), primary_key=True) # pk
    offering_date = db.Column(db.Unicode(100), primary_key=True)
    course_serial_number = db.Column(db.String(2), primary_key=True)
    course_name = db.Column(db.Unicode(100))
    training_program = db.Column(db.Unicode(100))
    course_credit = db.Column(db.String(4))
    course_type = db.Column(db.Unicode(4))
    exam_type = db.Column(db.Unicode(50))
    teacher = db.Column(db.Unicode(100))
    offering_weeks = db.Column(db.Unicode(100))
    offering_day_of_week = db.Column(db.Unicode(100))
    class_section = db.Column(db.Unicode(100))
    campus = db.Column(db.Unicode(100))
    teaching_building = db.Column(db.Unicode(100))
    classroom = db.Column(db.Unicode(100))

    def __repr__(self):
        return '<课程 {}>'.format(self.course_number)

class UserCourseSchedule(db.Model):

    __tablename__ = 'jwc_user_course_schedule'

    student_ID = db.Column(db.String(12), db.ForeignKey('jwc_user.student_ID'), primary_key=True)
    course_number = db.Column(db.String(9), db.ForeignKey('jwc_course.course_number'), primary_key=True)
    course_serial_number = db.Column(db.String(2), db.ForeignKey('jwc_course.course_serial_number'), primary_key=True)
    offering_date = db.Column(db.String(100), db.ForeignKey('jwc_course.offering_date'), primary_key=True)
    study_mode = db.Column(db.String(8))
    course_selection_state = db.Column(db.String(8))

    def __repr__(self):
        return '<{} 选课 {}>'.format(self.student_ID, self.course_number)

