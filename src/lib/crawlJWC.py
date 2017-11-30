#%%
import requests
from 

# 登陆, 获取课表页
sess = requests.Session()
data = {'zjh': '2015141462232', 'mm': '133637'}
sess.post('http://202.115.47.141/loginAction.do', data=data)
res = sess.get('http://202.115.47.141/xkAction.do?actionType=6')


#%%
# 解析课表
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'lxml')
classTable = soup.find_all('table', 'titleTop2')[1]

#%%
# 存储课表
classTableHeads = classTable.find('thead').find_all('th')

# 把课表表头写入文本
with open('课程表.csv', 'a+', encoding='utf-8') as f:
    classTableHeads.pop(8)
    for x in classTableHeads:
        f.write(x.get_text().strip())
        f.write(',')
    f.write('\n')
classTableBody = classTable.find_all('tr', 'odd')

# 把课表写入文本
with open('课程表.csv', 'a+', encoding='utf-8') as f:
    for tr in classTableBody:
        tds = tr.find_all('td')
        if len(tds) < 17:
            pass
        else:
            tds.pop(8)
            for td in tds:
                try:
                    f.write(td.get_text().strip())
                    f.write(',')
                    # 课表中的特殊字符需要处理
                    print(td.get_text().strip(), end=',')
                except AttributeError:
                    pass
            f.write('\n')
            print()


#%% 
# 插入数据库

from models.Model import User, Course, UserCourseSchedule

def insert_user():
    pass

def update_user():
    pass

def select_user():
    pass