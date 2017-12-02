from urllib.parse import quote_plus
import setting

appid = setting.appID
redirect_url = setting.user_binding_page

def user_binding():
    wx_url = 'http://open.weixin.qq.com/connect/oauth2/authorize?appid={AppID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={SCOPE}&state={STATE}#wechat_redirect'.format(AppID=appid, REDIRECT_URI=quote_plus(redirect_url),SCOPE='snsapi_userinfo', STATE='123')
    print('返回url: {}'.format(wx_url))
    return wx_url