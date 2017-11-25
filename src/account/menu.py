import requests

def create_menu(menu_json, access_token):
    """
    构造微信公众号自定义菜单
        :param menu_json: 构造自定义菜单的json对象
        :param access_token: 微信接口的access_token
    """
    import json
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={ACCESS_TOKEN}'.format(ACCESS_TOKEN=access_token)

    menu = json.dumps(menu_json, ensure_ascii=False)
    menu = menu.encode('utf-8')
    return requests.post(url, data=menu)

def delete_menu(access_token):

    url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token={}'.format(access_token)
    return requests.post(url)
