from db.database import db_session
from models.Model import *
from lib import crawlJWC

def has_student_in_db(studentID):
    u = User.query.filter(User.student_ID==studentID)
    if u is not None:
        return False
    else:
        return True

# refact this method
def insert_user_to_db(studentID, openid, passwd):
    stid = User.query.filter(User.student_ID==studentID).first()
    if stid is not None:
        print(studentID + "已经在数据库!")
    else:
        u = User(student_ID=studentID, wx_ID=openid, jwc_passwd=passwd)
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

            _q = UserCourseSchedule.query.filter(UserCourseSchedule.course_ID==course_ID).filter(UserCourseSchedule.student_ID==studentID).first()
            if _q is None:
                # course_id 没有在数据库
                print('{} 选 {} 课程没有在数据库'.format(studentID, course_ID))

                u = UserCourseSchedule(

                    student_ID=studentID,
                    course_ID= course_ID,
                    study_mode=study_mode,
                    course_selection_state=course_selection_state


                )
                db_session.add(u)
                db_session.commit()
            else:
                print('{} 选 {} 课程已经在数据库'.format(studentID, course_ID))


def insert_task_to_db(openid, task, task_day, task_month, task_year, task_hour, task_min):
    import hashlib

    hashstr = task + openid + task_day + task_month + task_year + task_hour + task_min
    sha1obj = hashlib.sha1()
    sha1obj.update(hashstr.encode('utf-8'))
    task_ID = sha1obj.hexdigest()

    t_id = Task.query.filter(Task.task_ID==task_ID).first()
    if t_id is not None:
        print(t_id + "已经在数据库!")
    else:
        t = Task(
            task_ID=task_ID,
            task = task,
            thour = task_hour,
            tmin = task_min,
            tyear = task_year,
            tmonth = task_month,
            tday = task_day
        )
        try:
            db_session.add(t)
            db_session.commit()
            return 1  # 成功返回 1
        except Exception as e:
            print('插入task到数据库错误: ' + str(e))
            return -1 # 失败返回 -1


# TODO: 添加任务的数据查询
def get_task(tday, tmonth, tyear):
    tasks = []
    _t = Task.query.filter(Task.tday==str(tday)).filter(Task.tmonth==str(tmonth)).filter(Task.tyear==str(tyear)).all()
    for x in _t:
        thour = x.thour
        tmin = x.tmin
        if thour !=  '-1':
            if tmin != '-1':
                ti = "{}:{}".format(thour, tmin)
            else:
                ti = "{}:{}".format(thour, '00')
        else:
            ti = "今天"
        _tt = {
            'task': x.task,
            'time': ti
        }
        tasks.append(_tt)
    return tasks
