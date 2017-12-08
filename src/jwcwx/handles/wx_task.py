from db import operator
from lib import MsgRender

def get_today_task(openid, frm):
    import time
    localtime = time.localtime()
    tday = localtime.tm_mday
    tmonth = localtime.tm_mon
    tyear = localtime.tm_year
    # TODO: model task 中添加月份,年份信息
    tasks = operator.get_task(tday, tmonth, tyear)
    if len(tasks) is 0:
        msg = '今天没有任务'
        return MsgRender.render(openid, frm, 'text', msg)
    else:
        msg = '提醒:'
        for x in tasks:
            msg = msg + x['task']
            msg = msg + '\n截止时间:'
            msg = msg + x[ 'time']
            msg = msg + "\n\n"

        return MsgRender.render(openid, frm, 'text', msg)
        
