from lib import MsgRender
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def reply(msgData):
    to = msgData['openID']
    frm = msgData['wxOfficeAccount']
    msgType = 'text'
    task_day = msgData['recognition']
    msg = '''创建任务成功:
    {}
    '''.format(task_day)

    return MsgRender.render(to, frm, msgType, msg)

def get_task_time(text):
    import re
    import time
    from lib.chinese_to_num import convertChineseDigitsToArabic
    localtime = time.localtime()
    tmin = localtime.tm_min
    thour = localtime.tm_hour
    tday = localtime.tm_mday
    tmonth = localtime.tm_mon
    tyear = localtime.tm_year
    wday = localtime.tm_wday + 1
    mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    task_day = re.search(r'(今天|明天|后天|大后天|tomorrow|day after tomorrow)', text)
    logger.debug('匹配到文本中的 day:', task_day)
    print('匹配到文本中的 day:', task_day)
    
    if task_day is not None:
        task_day = task_day.group()
        if task_day == '今天':
            task_day = tday
        elif task_day == '明天':
            task_day = tday + 1
        elif task_day == 'tommorrow':
            task_day = tday + 1
        elif task_day == '后天':
            task_day = tday + 2
        elif task_day == 'day after tomorrow':
            task_day = tday + 2
        elif task_day == '大后天':
            task_day = tday + 3
        print(task_day)
        
    else:
        task_day = re.search(r'(\d{1,2}(号|日)|[一, 二, 三, 四, 五, 六, 七, 八, 九, 十](号|日)|[一, 二, 三]十[一, 二, 三, 四, 五, 六, 七, 八, 九, 十](号|日)', text)
        if task_day is not None:
            task_day = task_day.group()

            tt = task_day
            tt = tt.strip(r'(号|日)')
            task_day = convertChineseDigitsToArabic(tt)
            if task_day > 31 or task_day < 0:
                task_day = tday
        else:
            task_day = re.search(r'(星期|周)[一,二,三,四,五,六,日,天]', text)
            if task_day is not None:
                td = convertChineseDigitsToArabic(task_day.strip(r'(星期|周)').replace(r'日|天', '七'))

                if td >= wday:
                    task_day = td - wday + tday
                else:
                    task_day = td - wday + 7 + tday
                if task_day > mdays[tmonth]:
                    task_day = task_day - mdays[tmonth]
            else:
                task_day = tday


        
    task_year = re.search(r'(\d{4}|[一, 二, 三, 四, 五, 六, 七, 八, 九, 十, 零]{4}, text)年', text)
    if task_year is not None:
        task_year = task_year.group()
        task_year = convertChineseDigitsToArabic(task_year.strip('年'))
    else:
        task_year = tyear
    
    task_month = re.search(r'(\d{1,2}|[一, 二, 三, 四, 五, 六, 七, 八, 九, 十, 十一,十二])月',text)
    if task_month is not None:
        task_month = task_month.group()
        task_month = convertChineseDigitsToArabic(task_month.strip('月'))
    else:
        task_month = tmonth
        if task_day > mdays[tmonth-1]:
            task_month = tmonth + 1
            task_day = task_day - mdays[tmonth]

    t_hour = re.search(r'(\d{1,2}点|[一, 二, 三, 四, 五, 六, 七, 八, 九, 十, 零]点|[一, 二]十[一, 二, 三, 四, 五, 六, 七, 八, 九, 十]点)半{0,1}', text)
    if t_hour is not None:
        t_hour = t_hour.group()
        t_hour = t_hour.strip(r'点|点半')
        t_hour = convertChineseDigitsToArabic(t_hour)
    else:
        t_hour = -1
    
    
    t_min = re.search(r'(点\d{1,2}|[一, 二, 三, 四, 五]十?[一, 二, 三, 四, 五, 六, 七, 八, 九, 十]分?)',text)
    if t_min is not None:
        t_min = t_min.group()
        t_min = convertChineseDigitsToArabic(t_min.strip(r'点|分'))
        if t_min >= 60:
            t_min = -1
    else:
        t_min = -1


    ti = {
        'tday': task_day,
        'tmonth': task_month,
        'tyear': task_year,
        'thour': t_hour,
        'tmin' : t_min
    }
    print(ti)


    return ti


def insert_task_to_db(msgData):
    from db import operator
    openid = msgData['openID']
    task = msgData['recognition']
    task_time = get_task_time(msgData['recognition'])
    task_month = str(task_time['tmonth'])
    task_day = str(task_time['tday'])
    task_year = str(task_time['tyear'])
    task_hour = str(task_time['thour'])
    task_min = str(task_time['tmin'])

    operator.insert_task_to_db(openid, task, task_day, task_month, task_year, task_hour, task_min)

        
