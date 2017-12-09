from db.operator import has_student_in_db,\
insert_user_to_db,\
insert_user_course_to_db,\
update_course_table
from lib.crawlJWC import crawlTable
from lib import MsgRender

def __bind_user(studentID, openid, jwc_passwd):
    '''
    return 0: studentid 已经在数据库.
    return -1: 登陆教务处失败
    return -2: 插入数据到数据库失败
    return 1: 绑定成功
    '''

    if has_student_in_db(studentID):
        # 学号已经在数据库
        return 0
    else:
        crawlT = crawlTable(studentID, jwc_passwd)
        if crawlT is None:
            # 登陆失败
            return -1
        else:
            try:
                insert_user_to_db(studentID, openid, jwc_passwd)
                update_course_table(crawlT)
                insert_user_course_to_db(studentID, crawlT)
                return 1
            except Exception as e:
                print('绑定用户失败: ', e)
                return -2

def bind_user_reply(studentID, wxOfficeAccount, openid, passwd):
    _r = __bind_user(studentID, openid, passwd)
    if _r == -1:
        print('登陆教务处失败')
        return MsgRender.render(openid, wxOfficeAccount, 'text', '登陆教务处失败')
    elif _r == 0:
        print('该学号已经被绑定')
        return MsgRender.render(openid, wxOfficeAccount, 'text', '该学号已经被绑定')
    elif _r == -2:
        print('绑定失败')
        return MsgRender.render(openid, wxOfficeAccount, 'text', '绑定失败')
    elif _r == 1:
        print('绑定成功')
        return MsgRender.render(openid, wxOfficeAccount, 'text', '绑定成功')