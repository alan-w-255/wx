# -*- coding: utf-8 -*-
# python3
import hashlib
import xml.etree.ElementTree as ET
from configparser import ConfigParser
from flask import Flask, request, render_template
from Handles import GetHandle, PostHandle

cfg = ConfigParser()
cfg.read('./setting.ini')

root_path = cfg.get('app', 'root_path')

app = Flask(__name__, root_path=root_path)

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

@app.route('/sign_up')
def sign_up():
    # wxUserAccount = request.args['wxuser']
    return render_template('bindUser.html')

@app.route('/user_binding')
def bind_user():
    print('访问 /user_binding 页面')
    return app.send_static_file('/html/user_binding.html')


app.debug = cfg.getboolean('debug', 'debug-mode')

# 实现用户绑定功能
