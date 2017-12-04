from models.database import db_session
from models.Model import *
from jwcwx.lib import crawlJWC

def has_student_in_db(studentID):
    u = User.query.filter(User.student_ID==studentID)
    if u is not None:
        return False
    else:
        return True

def insert_user_to_db(studentID, passwd):
    u = User(student_ID=studentID, passwd=passwd)
    try:
        db_session.add(u)
        db_session.commit()
        return 1  # 成功返回 1
    except Exception as e:
        print '插入User到数据错误: ' + str(e)
        return -1 # 失败返回 -1

def insert_course_table_to_db(studentID, passwd):
    from setting import semester
    course_table = crawlJWC(studentID, passwd)
    if course_table is None:
        return -1
    else:
        for r in course_table:
            course_number = r['课程号']
            course_serial_number = r['课序号']
            course_selection_state=r['选课状态']
            study_mode=r['修读方式']

            update_course_table(course_table)

            u = UserCourseSchedule(

                student_ID=studentID,
                course_number=course_number,
                course_serial_number=course_serial_number,
                study_mode=study_mode,
                course_selection_state=course_selection_state

            )
            db_session.add(u)
            db_session.commit()

def update_course_table(course_table):
    for r in course_table:
        course_number = r['课程号']
        course_serial_number = r['课序号']
        offering_date = semester

        r = Course.query.filter(Course.course_number==course_number and Course.course_serial_number==course_serial_number and Course.offering_date==offering_date)
        if r is None:
            # insert course to db
            c = Course(

                course_number = r['课程号']
                course_serial_number = r['课序号']
                offering_date = semester
                course_name = r['课程名']
                training_program = r['培养方案']
                course_credit = r['学分']
                course_type = r['课程属性']
                exam_type = r['考试类型']
                teacher = r['教师']
                offering_weeks = r['周次']
                offering_day_of_week = r['星期']
                class_section = r['节次']
                campus = r['校区']
                teaching_building = r['教学楼']
                classroom = r['教室']

            )

            db_session.add(c)
            db_session.commit()

        else:
            pass