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

@app.route('/getBindingData', methods=['post'])
def bind_user_data():
    from models.operator import has_student_in_db, insert_user_to_db, insert_user_info_to_db
    studentID = request.data['studentID']
    passwd = request.data['passwd']
    if has_student_in_db(studentID):
        return render_template('IDAlreadyBinded.html')
    else:
        try:
            insert_user_to_db(studentID, passwd)
            insert_user_info_to_db(studentID, passwd)
            return render_template('bindingSucceed.html')
        except Exception as e:
            print(e)
            return render_template('bindingFailed.html')


app.debug = setting.debug_mode

# 实现用户绑定功能
