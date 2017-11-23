# coding:utf-8

# from .BaseHandler import BaseHandler
# import handlers.BaseHandler
from handlers.BaseHandler import RequestBaseHandler

class IndexHandler(RequestBaseHandler):
    """"""

    def get(self, *args, **kwargs):
        # self.write("this home page")
        return self.render("statics/index2.html")
        # return self.redirect('./statics/index.html')

    def post(self, *args, **kwargs):
        self.write("this home page")



