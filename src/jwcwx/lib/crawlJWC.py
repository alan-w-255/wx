#%%
import requests
from bs4 import BeautifulSoup


#%%
def crawlTable(studentID, passwd):
    data = {
        'zjh': 2015141462232,
        'mm': 133637
    }

    sess = requests.Session()
    r = sess.post('http://202.115.47.141/loginAction.do', data=data)
    if len(r.text) > 1000:
        print('登陆失败')
        return None
    else:
        res = sess.get('http://202.115.47.141/xkAction.do?actionType=6')
        table = []
        soup=BeautifulSoup(res.text, 'lxml')
        classTable = soup.find_all('table', 'titleTop2')[1]

        classTableHeads = classTable.find('thead').find_all('th')
        classTableHeads.pop(8)
        headers = []
        for h in classTableHeads:
            headers.append(h.text.strip())

        classTableBody = classTable.find_all('tr', 'odd')
        for tr in classTableBody:
            tds = tr.find_all('td')
            course_record = {}
            if len(tds) < 17:
                continue
            else:
                tdlist = []
                tds.pop(8)
                for x in tds:
                    tdlist.append(x.text.strip())
                
                for th, td in zip(headers,tdlist):
                    course_record[th.strip()] = td.strip()
            table.append(course_record)
        return table

# r = crawlTable('2015141462232', '133637')
# with open('table.json', 'a+') as f:
#     for x in r:
#         f.write(str(x))