# coding: utf-8

import re
import hashlib
from handlers.BaseHandler import RequestBaseHandler
from constants import Res
from dbHandler.DBTools import DBTool
# from config import password_has_key
import config
import copy
import datetime

import tornado.gen
from tornado.httpclient import AsyncHTTPClient
import time
import json
import random
from hashlib import md5

class UserLoginHandler(RequestBaseHandler):
    """用户验证码登录接口(未注册用户先注册后登录)"""
    def post(self, *args, **kwargs):
        mobile = self.json_args.get('mobile')
        verifyCodde = self.json_args.get('verify_code')
        if not all([mobile, verifyCodde]):
            return self.write(dict(code=Res.PARAMERR, msg="参数不全", data={}))
        # 手机正则验证
        if not re.match(r"^1\d{10}$", mobile):
            return self.write(dict(code=Res.PARAMERR, msg="参数错误", data={}))
        # 6位验证码正则验证
        if not re.match(r"^\d{6}$", verifyCodde):
            return self.write(dict(code=Res.PARAMERR, msg="参数错误", data={}))

        sql = "SELECT * FROM T_user_info WHERE user_mobil=%s" % mobile
        result = DBTool.query_one(sql)  # 查询一个，返回字典

        # 查询成功,但无数据
        if result == None:
            print("kjfk")
        # result为空,排除上面的无数据的情况后,为空即为查询失败
        if not result:
            return self.write(dict(code=Res.SERVERERR, msg="登录失败,请稍后重试", data={}))

        if result.get('user_mobile') == mobile:
            pass


class RegisterHandler(RequestBaseHandler):
    """注册接口"""
    def post(self, *args, **kwargs):
        # 获取参数
        mobile = self.json_args.get("mobile")
        password = self.json_args.get("password")

        if not all([mobile, password]):
            return self.write(dict(code=Res.PARAMERR, msg="参数不完整", data={}))
        if not re.match(r"^1\d{10}$", mobile):
            return self.write(dict(code=Res.DATAERR, msg="手机号格式错误", data={}))

        sql = "SELECT * FROM T_user_info WHERE user_mobile=\"%s\"" % mobile
        user_result = DBTool.query_all(sql)
        if user_result and len(user_result) > 0:
            return self.write(dict(code=Res.DATAEXIST, msg="手机号已存在", data={}))

        passwd = hashlib.sha256((password + config.password_has_key).encode('utf-8')).hexdigest()
        sql = "INSERT INTO T_user_info(user_name, user_mobile, user_password) VALUE (\"%s\", \"%s\", \"%s\")" % (mobile, mobile, passwd)
        if DBTool.excute_sql(sql):
            return self.write(dict(code=Res.OK, msg='注册成功', data={}))
        else:
            return self.write(dict(code=Res.DATAEXIST, msg="注册失败，请稍后重试", data={}))



class LoginHandler(RequestBaseHandler):
    """账号密码登录接口"""
    def post(self, *args, **kwargs):
        mobile = self.json_args.get("mobile")

        login_type = self.json_args.get("login_type")

        if not all([mobile, login_type]):
            return self.write(dict(code=Res.LOGINERR, msg='参数不全'))
        else:
            print(mobile)
            sql = "SELECT * FROM T_user_info WHERE user_mobile=%s" % mobile
            query_result = DBTool.query_one(sql) #查询一个，返回字典
            # if result.__len__() == 0:
            #     self.write(dict(errcode=Res.LOGINERR, errmsg='用户不存在'))
            if query_result:
                if login_type == 1: #账号密码登录
                    password = self.json_args.get("password")

                    if not password:
                        return self.write(dict(code=Res.LOGINERR, msg='参数不全'))
                    else:
                        passwd = hashlib.sha256((password + config.password_has_key).encode('utf-8')).hexdigest()
                        db_user_pwd = query_result.get("user_password")
                        if passwd == db_user_pwd:
                            # response_data = {}
                            # for k,v in result.items():
                            #     if not v:
                            result = copy.deepcopy(query_result)
                            del result['user_create_time']
                            del result['user_update_time']
                            del result['user_password']
                            register_time = query_result.get("user_create_time")
                            if register_time:
                                result['user_create_time'] = str(register_time)
                            return self.write(dict(code=Res.OK, msg='登录成功', data=result))
                        else:
                            return self.write(dict(code=Res.LOGINERR, msg='密码错误', data={}))

                elif login_type == 2: #手机+验证码登录
                    result = copy.deepcopy(query_result)
                    del result['user_create_time']
                    del result['user_update_time']
                    del result['user_password']
                    register_time = query_result.get("user_create_time")
                    if register_time:
                        result['user_create_time'] = str(register_time)
                    return self.write(dict(code=Res.OK, msg='登录成功', data=result))

                else: #其他方式 可能有三方登录，先不考虑
                    return self.write(dict(code=Res.LOGINERR, msg='参数不全'))

            else:
                return self.write(dict(code=Res.LOGINERR, msg='登录失败，用户不存在', data={}))



class VerifyCodeLoginHandler(RequestBaseHandler):
    """手机+验证码登录接口"""
    def post(self, *args, **kwargs):
        mobile = self.json_args.get("mobile")

        if not mobile:
            return self.write(dict(code=Res.LOGINERR, msg='参数不全', data={}))
        else:
            sql = "SELECT * FROM T_user_info WHERE user_mobil=%s" % mobile
            result = DBTool.query_one(sql) #查询一个，返回字典

            if result.__len__() == 1:
                assert "输出有问题，datetime不能直接放到json中输出"
                return self.write(dict(code=Res.OK, msg='登录成功', data=result))

            else:
                return self.write(dict(code=Res.LOGINERR, msg='用户不存在', data={}))

class LogoutHandler(RequestBaseHandler):
    """退出接口"""

class UpdateUserInfoHandler(RequestBaseHandler):
    """更新用户信息接口"""
    def post(self, *args, **kwargs):
        user_id = self.json_args.get('user_id')
        user_avatar_url = self.json_args.get('user_avatar')
        user_name = self.json_args.get('user_name')
        user_mobile = self.json_args.get('user_mobile')
        user_gender = self.json_args.get('user_gender')
        user_age = self.json_args.get('user_age')
        user_real_name = self.json_args.get('user_real_name')
        user_area = self.json_args.get('user_area')
        user_profil = self.json_args.get('user_profil')

        sql = "UPDATE T_user_info SET "
        if user_avatar_url:
            sql += "user_avatar='%s' "%user_avatar_url
        if user_name:
            sql += "user_name='%s' "%user_name
        if user_mobile:
            sql += "user_mobile='%s' "%user_mobile
        if user_gender:
            sql += "user_avatar=%d "%(int(user_gender))
        if user_age:
            sql += "user_age=%d "%(int(user_age))
        if user_real_name:
            sql += "user_real_name='%s' "%user_real_name
        if user_area:
            sql += "user_area='%s' "%user_area
        if user_profil:
            sql += "user_profil='%s' "%user_profil

        if sql == "UPDATE T_user_info SET ":
            return self.write(dict(code=Res.DATAERR, msg='参数不全,请至少添加一个要修改的信息', data={}))
        else:
            # sql = "UPDATE T_user_info SET user_avatar='%s' WHERE user_id='%s'" %(user_avatar_url, user_id)
            update_date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql += "user_update_time='%s' "%update_date_str

            if DBTool.excute_sql(sql):
                return self.write(dict(code=Res.OK, msg='更新成功', data={}))
            else:
                return self.write(dict(code=Res.IOERR, msg='更新失败', data={}))


class GetUserInfo(RequestBaseHandler):
    """获取用户信息接口"""
    def post(self, *args, **kwargs):
        user_id = self.json_args.get('user_id')
        user_mobile = self.json_args.get('user_mobile')

        if not user_id:
            if not user_mobile:
                return self.write(dict(code=Res.DATAERR, msg='参数不全', data={}))
            else:
                sql = "SELECT * FROM T_user_info WHERE user_mobile='%s'"% user_mobile
        else:
            sql = "SELECT * FROM T_user_info WHERE user_id='%s'" % user_id
            if user_mobile:
                sql += " and user_mobile='%s'"%user_mobile

        query_result = DBTool.query_one(sql)  # 查询一个，返回字典
        if not query_result:
            return self.write(dict(code=Res.IOERR, msg='获取失败，用户不存在', data={}))
        else:
            result = copy.deepcopy(query_result)
            del result['user_create_time']
            del result['user_update_time']
            del result['user_password']
            del result['user_token']
            register_time = query_result.get("user_create_time")
            if register_time:
                result['user_create_time'] = str(register_time)
            return self.write(dict(code=Res.OK, msg='获取成功', data=result))

class GetVerifyCodeHandler(RequestBaseHandler):
    """获取验证码接口"""
    def post(self, *args, **kwargs):
        mobile = self.json_args.get('user_mobile')
        if not re.match(r"^1\d{10}$", mobile):
            return self.write(dict(code=Res.DATAERR, msg="手机号格式错误", data={}))
        verify_code = str("%06d"%random.randint(0,999999))

        # 应该是调用验证码提供商的接口
        md = hashlib.md5()
        md.update(verify_code)

        return self.write(dict(code=Res.OK, msd='获取验证码成功', data={"verify_code":md.hexdigest()}))

class AccessToken(object):
    """access_token管理类"""
    _access_token = None
    _create_time = 0
    _expires_in = 0

    @classmethod
    @tornado.gen.coroutine
    def update_access_token(cls):
        client = AsyncHTTPClient()
        url = "https://api.weixin.qq.com/cgi-bin/token?" \
        "grant_type=client_credential&appid=%s&secret=%s" # % (WECHAT_APP_ID, WECHAT_APP_SECRET) #一部接口API
        resp = yield client.fetch(url)
        dict_data = json.loads(resp.body)
        if "errcode" in dict_data:
            raise Exception("wechat server error")
        else:
            cls._access_token = dict_data["access_token"]
            cls._expires_in = dict_data["expires_in"]
            cls._create_time = time.time()


    @classmethod
    @tornado.gen.coroutine
    def get_access_token(cls):
        if True: #过期时间判定
            # 向微信服务器请求access_token
            yield cls.update_access_token()
            raise tornado.gen.Return(cls._access_token)
        else:
            raise tornado.gen.Return(cls._access_token)

