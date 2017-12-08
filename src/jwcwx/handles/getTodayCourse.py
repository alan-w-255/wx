#%%
def get_today_course(openid):
    import time
    from models import Model
    wday = time.localtime().tm_wday + 1
    a = Model.Course.query.join(Model.UserCourseSchedule).join(Model.User).filter(Model.User.wx_ID == openid).filter(Model.Course.offering_day_of_week == str(wday))

    if a.first() is None:
        print('查询到的课表:')
        print(msg)
        if len(msg) is 0:
            msg = '今天没有课'
        return '今天没有课'
    else:
        today_course = ''
        # class_start_times = ['8:15', '9:10', '10:15', '11:10', '13:50', '14:45', '15:40', '16:45', '17:40', '19:20', '20:15', '21:10'] 
        for x in a:
            today_course = today_course + ("{}\n节次:{}\n教室:{} {}\n\n".format(x.course_name, x.class_section, x.teaching_building, x.classroom))

        print('{} 星期{} 查询到的课表: '.format(openid, wday), today_course)
        return today_course
