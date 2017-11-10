# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle

# NOTE: 路由
urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    # NOTE: 注册路由
    app = web.application(urls, globals())
    app.run()
