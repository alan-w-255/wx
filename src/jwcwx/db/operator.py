from db.database import db_session
from models.Model import *
from lib import crawlJWC

def has_student_in_db(studentID):
    u = User.query.filter(User.student_ID==studentID)
    if u is not None:
        return False
    else:
        return True

def insert_user_to_db(studentID, passwd):
    stid = User.query.filter(User.student_ID==studentID).first()
    if stid is not None:
        print(studentID + "已经在数据库!")
    else:
        u = User(student_ID=studentID, jwc_passwd=passwd)
        try:
            db_session.add(u)
            db_session.commit()
            return 1  # 成功返回 1
        except Exception as e:
            print('插入User到数据错误: ' + str(e))
            return -1 # 失败返回 -1

def update_course_table(course_table):
    from setting import semester
    import hashlib

    for r in course_table:

        course_number = r['课程号']
        course_serial_number = r['课序号']
        offering_date = semester

        hashstr = course_number+course_serial_number+offering_date

        sha1obj = hashlib.sha1()
        sha1obj.update(hashstr.encode('utf-8'))
        hashID = sha1obj.hexdigest()


        _q = Course.query.filter(Course.ID==hashID).first()
        if _q is None:
            # insert course to db
            print("{} {} {}没有在数据库".format(course_number, course_serial_number, offering_date))
            c = Course(
                ID = hashID,
                course_number = r['课程号'],
                course_serial_number = r['课序号'],
                offering_date = semester,
                course_name = r['课程名'],
                training_program = r['培养方案'],
                course_credit = r['学分'],
                course_type = r['课程属性'],
                exam_type = r['考试类型'],
                teacher = r['教师'],
                offering_weeks = r['周次'],
                offering_day_of_week = r['星期'],
                class_section = r['节次'],
                campus = r['校区'],
                teaching_building = r['教学楼'],
                classroom = r['教室']
            )

            db_session.add(c)
            db_session.commit()

        else:
            print("{} {} {} 在数据库".format(course_number, course_serial_number, offering_date))

def insert_user_course_to_db(studentID, course_table):
    from setting import semester
    import hashlib

    offering_date = semester

    if course_table is None:
        return -1
    else:
        for r in course_table:
            course_number = r['课程号']
            course_serial_number = r['课序号']
            course_selection_state=r['选课状态']
            study_mode=r['修读方式']

            hashstr = course_number+course_serial_number+offering_date
            sha1obj = hashlib.sha1()
            sha1obj.update(hashstr.encode('utf-8'))

            course_ID = sha1obj.hexdigest()

            u = UserCourseSchedule(

                student_ID=studentID,
                course_ID= course_ID,
                study_mode=study_mode,
                course_selection_state=course_selection_state


            )
            db_session.add(u)
            db_session.commit()
