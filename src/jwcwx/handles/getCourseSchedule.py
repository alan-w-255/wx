def _get_week_order(year, month, day):
    # TODO:  get_week_order
    import datetime
    import setting
    open_scholl_date = setting.school_open_day
    _t = datetime.datetime(year, month, day) - datetime.datetime(open_scholl_date[0], open_scholl_date[1], open_scholl_date[2])
    cur_week = (_t.days + 6)//7
    return cur_week

def get_week_course(openid, year, month, day):
    import datetime
    from models import Model
    _d = datetime.datetime(year, month, day)
    _wd = _d.weekday()
    monday = _d - datetime.timedelta(days=_wd)
    cur_week = _get_week_order(year, month, day)

    weekdays_ch = ['一', '二', '三', '四', '五', '六', '日']

    week_course = ''

    _has_openid = Model.User.query.filter(Model.User.wx_ID==openid)
    if _has_openid.first() is None:
        return '您尚未绑定教务处账号, 无法使用课表查询功能' + \
            '请绑定你的教务处账号来使用课表查询服务!' + \
            '\n发送: 绑定 学号:教务处密码' + \
            '\n学号和教务处密码替换为你的学号和你的教务处密码(我们不会告诉任何人的)'

    for x in range(7):
        _cur_day = monday + datetime.timedelta(days=x)
        a = Model.Course.query.join(Model.UserCourseSchedule).join(Model.User).filter(Model.User.wx_ID == openid).filter(Model.Course.offering_day_of_week == str(_cur_day.weekday()+1))
        if a.first() is None:
            pass
        else:
            counter = 1
            a.order_by(Model.Course.class_section)
            for y in a:
                if _is_course_end(y, cur_week):
                    continue
                if counter == 1:
                    week_course = week_course + "周 {}\n".format(weekdays_ch[_cur_day.weekday()])
                    counter = 0
                week_course = week_course + "{}\n节次:{}\n教室:{} {}\n\n".format(y.course_name, y.class_section, y.teaching_building, y.classroom)
    
    if len(week_course) == 0:
        return '这周没课'
    else:
        return week_course
            


#%%
def get_course(openid, year, month, day):
    from models import Model
    from  datetime import datetime

    cur_week = _get_week_order(year, month, day)
    weekdays_ch = ['一', '二', '三', '四', '五', '六', '日']

    wday = datetime(year, month, day).weekday()
    # 判断是否绑定教务处
    _b = Model.User.query.filter(Model.User.wx_ID==openid)
    if _b.first() is None:
        return '您尚未绑定教务处账号, 无法使用课表查询功能' + \
            '请绑定你的教务处账号来使用课表查询服务!' + \
            '\n发送: 绑定 学号:教务处密码' + \
            '\n学号和教务处密码替换为你的学号和你的教务处密码(我们不会告诉任何人的)'

    a = Model.Course.query.join(Model.UserCourseSchedule).join(Model.User).filter(Model.User.wx_ID == openid).filter(Model.Course.offering_day_of_week == str(wday + 1))

    today_course_title = '周 {}:\n'.format(weekdays_ch[wday])
    today_course = ''


    print(a.first())
    if a.first() is None:
        pass
    else:
        for x in a:
            if _is_course_end(x, cur_week):
                continue
            today_course = today_course + ("{}\n节次:{}\n教室:{} {}\n\n".format(x.course_name, x.class_section, x.teaching_building, x.classroom))

        print('{} 星期{} 查询到的课表: '.format(openid, wday), today_course)
    if len(today_course) == 0:
        return '没有课'

    return today_course_title + today_course

def _is_course_end(course, cur_week):
    offer_week = course.offering_weeks
    offer_week = offer_week.strip(r'周|周上')
    offer_weeks = offer_week.split('-')
    if len(offer_weeks) == 1:
        offer_weeks = offer_week.split(',') 
        if str(cur_week) in offer_weeks:
            return False
    else:
        start_week = int(offer_weeks[0])
        end_week = int(offer_weeks[1])
        if int(cur_week) >= start_week and int(cur_week) <= end_week:
            return False
    return True
    


