# coding:utf-8

# from .BaseHandler import BaseHandler
# import handlers.BaseHandler
from handlers.BaseHandler import RequestBaseHandler
import os

class ImageHandler(RequestBaseHandler):
    """"""

    def get(self, *args, **kwargs):
        suburl = self.request.uri.split('/')[-1:][0]
        print(suburl)
        pic = open(os.path.join(os.path.dirname("handlers"), "statics/images/" + suburl), 'r')
        print("------")
        # pic = open("../statics/css/" + suburl,'r')
        pics = pic.read()
        print(pics)
        self.set_header("Content-type", "image/png")
        return self.write(pics.encode('utf8'))

    def post(self, *args, **kwargs):
        self.write("this home page")

class CssHandler(RequestBaseHandler):
    """获取css文件接口"""
    def get(self, *args, **kwargs):
        suburl = self.request.uri.split('/')[-1:][0]
        print(suburl)
        pic = open(os.path.join(os.path.dirname("handlers"), "statics/css/" + suburl),'r')
        # pic = open("../statics/css/" + suburl,'r')
        pics = pic.read()
        # self.set_header("Content-type", "image/png")
        return self.write(pics)

