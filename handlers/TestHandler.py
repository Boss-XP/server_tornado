# coding:utf-8


from handlers.BaseHandler import RequestBaseHandler
# from constants import Res
# from dbHandler.DBTools import DBTool
import time


class TestHandler(RequestBaseHandler):
    """发布数据接口"""
    def post(self, *args, **kwargs):
        # time.sleep(20)
        res = ["resp", {"hahah":123, "qwe":"测试接口数据"},123]
        return self.write(dict(code=0, msg='获取成功', data=res))
    def get(self, *args, **kwargs):
        res = ["resp", {"hahah": 123, "qwe": "dksfjslkdflk"}, 123]
        return self.write(dict(code=0, msg='获取成功', data=res))
