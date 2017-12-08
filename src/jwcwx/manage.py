from flask_script import Manager, Server, Shell
from db import database
from main import app
import setting

manager = Manager(app)

from models import Model
from db.operator import insert_user_course_to_db, insert_user_to_db, update_course_table
from lib.crawlJWC import crawlTable

stid = '2015141462232'
passwd = '133637'

jwct = crawlTable(stid, passwd)

def _make_context():
    return dict(app=app, Model=Model, insert_user_course_to_db=insert_user_course_to_db, insert_user_to_db=insert_user_to_db, update_course_table=update_course_table, jwct=jwct, stid=stid, passwd=passwd)

manager.add_command('shell', Shell(make_context=_make_context))

manager.add_command("runserver", Server(host='0.0.0.0', port=80))

@manager.command
def hello():
    print("hello")

@manager.command
def create_menu():
    from account.menu import create_menu
    from account.access_token import get_access_token
    import json
    import codecs
    appid = setting.appID
    appsecret = setting.appsecret
    access_token = get_access_token(appid, appsecret)
    menu_json = json.load(codecs.open(setting.menu, encoding='utf-8'))

    r = create_menu(menu_json, access_token)
    if json.loads(r.text)['errcode'] == 0:
        print('创建menu成功')
    else:
        print('创建menu失败')
        print(r.text)

@manager.command
def delete_menu():
    from account.menu import delete_menu
    from account.access_token import get_access_token
    import json

    appid = setting.appID
    appsecret = setting.appsecret
    access_token = get_access_token(appid, appsecret)

    r = delete_menu(access_token)
    if json.loads(r.text)['errcode'] == 0:
        print('删除menu成功')
    else:
        print('删除菜单失败')
        print(r.text)

@manager.command
def create_db():
    from db.database import init_db
    init_db()
    print('建立数据库成功!')

@manager.command
def drop_all_db_table():
    from db.database import drop_all
    drop_all()
    print('删除所有表成功!')

if __name__ == "__main__":
    manager.run()

