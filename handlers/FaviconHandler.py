# coding: utf-8

from handlers.BaseHandler import RequestBaseHandler
import os


class GetFavicon(RequestBaseHandler):
    """发布数据接口"""
    def get(self, *args, **kwargs):
        print('---fav')
        pic = open(os.path.join(os.path.dirname(__file__), "favicon.png"), 'r')
        return self.write(pic.read())