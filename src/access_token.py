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

    resp = requests.get(url)
    access_teken = json.loads(resp.text)['access_token']
    return access_teken
