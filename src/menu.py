import requests

def create_menu(menu_json, access_token):
    """
    构造微信公众号自定义菜单
        :param menu_json: 构造自定义菜单的json对象
        :param access_token: 微信接口的access_token
    """
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={ACCESS_TOKEN}'.format(ACCESS_TOKEN=access_token)

    requests.post(url, json=menu_json)
