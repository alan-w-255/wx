# -*- coding: utf-8 -*-
# python3
import hashlib
import xml.etree.ElementTree as ET
from configparser import ConfigParser
from flask import Flask
from flask import request
from Handles import GetHandle, PostHandle

cfg = ConfigParser()
cfg.read('./setting.ini')

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

app.debug = cfg.getboolean('debug', 'debug-mode')

# 实现用户绑定功能
