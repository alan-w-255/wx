# -*- coding: utf-8 -*-
# python3
import os
import hashlib
import xml.etree.ElementTree as ET
from flask import Flask, request, render_template
from handles import GetHandle, PostHandle
from db import database
from models import Model

import setting

root_path = setting.root_path
app = Flask(__name__, root_path=root_path)

database.init_db()

basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



@app.teardown_request
def shutdown_session(exception=None):
    database.db_session.remove()

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
    return render_template('bindUser.html')

@app.route('/getBindingData', methods=['post', 'GET'])
def bind_user_data():
    pass

@app.route('/getTodayCourse')
def get_today_course():
    from handles import PostHandle

    return PostHandle(request)
    

@app.route('/getTomCourse')
def get_tom_course():
    pass


app.debug = setting.debug_mode
