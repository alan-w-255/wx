from flask_script import Manager, Server, Shell
from db import database
from models.Model import User, Course, UserCourseSchedule
from main import app

shell = Shell(use_ipython=True)



manager = Manager(app)

def _make_context():
    return dict(app=app, database=database, dbUser=User, dbCourse=Course, dbUserCourseSchedule=UserCourseSchedule)

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
    from models.Model import db
    db.create_all()



if __name__ == "__main__":
    manager.run()