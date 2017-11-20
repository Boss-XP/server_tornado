# coding:utf-8

import json
import re
from tornado.web import RequestHandler



class RequestBaseHandler(RequestHandler):
    """handler基类"""

    @property
    def db(self):
        """作为requesthandler对象的db属性"""
        return self.application.db

    @property
    def redis(self):
        """作为requesthandler对象的redis属性"""
        return self.application.redis

    @property
    def request_data(self):
        """请求数据属性"""
        return self.request.body

    def initialize(self):
        pass

    def prepare(self):
        """预解析json数据"""
        if self.request.headers.get("Content-Type", "").__contains__("application/json"):

            body = self.request.body
            # print(body)
            # if not body:
            #     self.json_args = {}
            #     return
            if type(body) == bytes:
                body = body.decode("utf-8")
            self.json_args = json.loads(body)
            # self.json_args = json.loads(self.request.body)
        else:
            self.json_args = {}

    def write_error(self, status_code, **kwargs):
        pass

    def set_default_headers(self):
        """设置默认json格式"""
        self.set_header("Contnet-Type", "application/json; charset=UTF-8")

    def on_finish(self):
        pass



