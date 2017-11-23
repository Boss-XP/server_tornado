# coding:utf8

import os

# Application配置参数
"""
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "statics"),
    "template_path": os.path.join(os.path.dirname(__file__), "template"),

    "cookie_secret": "skjdfljsflajsdfka",
    "xsrf_cookies": True,

    "debug": True,
}"""

# dict()方式可以通过字典方式访问，方便
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "template"),
    static_path = os.path.join(os.path.dirname(__file__), "statics"),

    cookie_secret = "skjdfljsflajsdfka",
    # xsrf_cookies = True,

    debug = True
)


# 数据库配置参数
mysql_options = dict(
    host = "127.0.0.1",
    database = "iHome",
    user = "root",
    password = "Yx983420348*",
    charset = "utf8"
)

# Redis配置参数
redis_options = dict(
    host = "127.0.0.1",
    port = 6379
)


# 日志配置
log_path = os.path.join(os.path.dirname(__file__), "logs/log")
log_level = "debug"

# 密码加密秘钥
password_has_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="