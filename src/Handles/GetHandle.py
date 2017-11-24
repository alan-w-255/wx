import hashlib
from flask import request

def handle(request):
    assert request.method == 'GET', '传入请求的方法应为GET'
    try:
        ARGS = request.args
        SIGNATURE = ARGS['signature']
        TIMESTAMP = ARGS['timestamp']
        NONCE = ARGS['nonce']
        ECHOSTR = ARGS['echostr']
        TOKEN = "hellowx"
        assert isinstance(ECHOSTR, str), 'ECHOSTR 应该是一个字符串类型'
        _list = [TOKEN, TIMESTAMP, NONCE]
        _list.sort()
        list_str = "".join(_list)
        print(list_str)
        hashcode = hashlib.sha1(list_str.encode('utf_8')).hexdigest()
        print('hashcode = {}, signature = {}'.format(hashcode, SIGNATURE))

        if hashcode == SIGNATURE:
            print('验证通过, 返回echostr')
            return ECHOSTR
        else:
            print('验证失败')
            return ""
    except Exception as err:
        print("exception occurs while handle the GET /auth")
        return str(err)