from models.database import db_session
from models.Model import *

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

