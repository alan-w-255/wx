from flask_script import Manager, Server
from main import app
import setting

manager = Manager(app)

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

if __name__ == "__main__":
    manager.run()