# -*- coding: utf-8 -*-
# python3
import hashlib
import xml.etree.ElementTree as ET
from flask import Flask
from flask import request
from Handles import GetHandle, PostHandle

app = Flask(__name__)

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    assert request.path == '/auth', "应该路由 /auth"

    # 处理微信后台的认证请求
    if request.method == 'GET':
        return GetHandle.handle(request)
    elif request.method == 'POST':
        return PostHandle.handle(request)
    else:
        raise Exception('无法处理的request 方法: ', request.method)

app.debug = True

app.run(host='0.0.0.0', port=80)
