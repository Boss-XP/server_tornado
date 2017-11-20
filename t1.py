# coding:utf-8

import os
import tornado.web
import tornado.ioloop
import json


class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""
    def set_default_headers(self):
        self.set_header('bxp', 'bxp-server')

    def get(self):
        """get请求方式"""
        arg = self.get_query_arguments("a")
        arg2 = self.get_arguments('a')
        print(arg)
        print(arg2)
        self.write("hello mother fucker")
        # return self.render('statics/index.html')

    def post(self, *args, **kwargs):
        print(self.request.headers.get('a',default="aa1"))
        arg = self.get_query_arguments("a")
        arg2 = self.get_arguments('a')
        print(arg)
        print(arg2)

        content_type = self.request.headers.get('Content-Type', default='content-type')
        print('type'+str(content_type))
        if content_type.__contains__('application/json'):
            print(json.loads(self.request.body))

        self.write(u"gun滚滚")
        return self.write("djslkfsk" + str(arg2))

class SubjectHandler(tornado.web.RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self, *args, **kwargs):
        self.write(self.subject)

class Err404Handler(tornado.web.RequestHandler):
    pass


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    app = tornado.web.Application(
        [
            (r"^/*$", IndexHandler),
            # (r"^/()$", tornado.web.StaticFileHandler, {"path":os.path.join(current_path, "statics"), "default_filename":'index.html'}),
            (r"/login", SubjectHandler, {"subject": "login"}),
        ],
        static_path=os.path.join(os.path.dirname(__file__), "statics"),
        debug = True
    )



    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

