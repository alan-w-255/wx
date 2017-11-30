import os
from flask.ext.sqlalchemy import sqlalchemy
from main import app

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_RUI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'jwc_user'
    student_ID = db.Column(db.String(12), primary_key=True) # pk
    jwc_passwd = db.Column(db.String(20))

    # def __init__(self, student_ID, jwc_passwd):
    #     self.student_ID = student_ID
    #     self.jwc_passwd = jwc_passwd
    # 好像可以省略
    

    def __repr__(self):
        return '<user {}>'.format(self.student_ID)

class Course(db.Model):
    '''
        course_number
        course_name
        training_program
        course_serial_number
        course_credit
        course_type
        exam_type
        teacher
        offering_weeks
        offering_day_of_week
        class_section
        campus
        teaching_building
        classroom
    '''
    __tablename__ = 'jwc_course'
    course_number = db.Column(db.String(9)) # pk
    course_name = db.Column(db.Unicode(100)) # pk
    training_program = db.Column(db.Unicode(100))
    course_serial_number = db.Column(db.String(2))
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

    # def __init__(self, **kws):
    #     course_number = kws['course_number']
    #     course_name = kws['course_name']
    #     training_program = kws['training_program']
    #     course_serial_number = kws['course_serial_number']
    #     course_credit = kws['course_credit']
    #     course_type = kws['course_type']
    #     exam_type = kws['exam_type']
    #     teacher = kws['teacher']
    #     offering_weeks = kws['offering_weeks']
    #     offering_day_of_week = kws['offering_day_of_week']
    #     class_section = kws['class_section']
    #     campus = kws['campus']
    #     teaching_building = kws['teaching_building']
    #     classroom = kws['classroom']
    # 好像可以省略
        

    def __repr__(self):
        return '<课程 {}>'.format(self.course_number)

class UserCourseSchedule(db.Model):
    __tablename__ == 'user_course_schedule'
    student_ID = db.Column(db.String(12))
    course_number = db.Column(db.String(9))
    course_serial_number = db.Column(db.String(2))
    study_mode = db.Column(db.String(8))
    course_selection_state = db.Column(db.String(8))

    def __repr__(self):
        return '<{} 选课 {}>'.format(self.student_ID, self.course_number)

