import json
import requests

def get_access_token(appid, appsecret):
    """
    调用微信api, 获取access token.
        :param appid: 微信服务号, 公众号,小程序的appid
        :param appsecret: 微信服务号, 公众号, 小程序的appsecret
    """

    url = 'https://api.weixin.qq.com/cgi-bin/token\
?grant_type=client_credential\
&appid={APPID}&secret={APPSECRET}'.format(APPID=appid, APPSECRET=appsecret)

    print('get url: {}'.format(url))
    resp = requests.get(url)
    data = json.loads(resp.text)
    try:
        access_teken = data['access_token']
        print('获取access_token成功, access_token: {}'.format(access_teken))
        return access_teken
    except KeyError:
        print('返回数据没有key:access_token')
        print(data)

