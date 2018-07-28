# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

# 数据库相关两个库
# import torndb
# import redis
import pymysql

import os
import datetime

from tornado.options import define, options
from tornado.web import RequestHandler

# 自定义文件导入
import urls #url配置文件
import config #服务器相关配置文件

define("port", type=int, default=8082, help="run server on the given port")


class Application(tornado.web.Application):
    """自定义Application，便于自定义封装和数据库等封装"""
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        # self.db = torndb.Connection(**config.mysql_options)
        self.bd = pymysql.connect(**config.mysql_options)
        self.redis = ''#redis.StrictRedis(**config.redis_options)

def main():

    # file = open('logfile.txt','a')
    # file.write('\n--start--%s'%str(datetime.datetime.now()))
    # file.close()
    # print(os.path.join(os.path.dirname(__file__), "server.csr"))

    tornado.options.parse_command_line()
    app = tornado.web.Application(
        urls.urls_hander,
        **config.settings
    )

    http_server = tornado.httpserver.HTTPServer(app)
    # http_server = tornado.httpserver.HTTPServer(app, ssl_options={
    #     # "certfile": "/usr/local/Cellar/nginx/server.csr",
    #     # "keyfile": "/usr/local/Cellar/nginx/server.key",
    #     "certfile": os.path.join(os.path.abspath("."), "server.csr"),
    #     "keyfile": os.path.join(os.path.abspath("."), "server.key"),
    # })

    http_server.listen(options.port)

    tornado.ioloop.IOLoop.current().start()



if __name__ == '__main__':
    main()



