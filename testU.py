# coding:utf-8

# import dbHandler.DBTools
from dbHandler.DBTools import DBTool
import datetime
import tornado
import tornado.gen

# dbHandler.DBTools.DBTool
mobile = "18272165102"
passwd = "jkfdsjaksdf"

# sql = """INSERT INTO T_user_info(\
#           user_name, user_password, user_gender, user_age, user_mobile, user_avatar, user_isdeleted) \
#           VALUE ('bxp4', '1233212', %d, 122, %s, 'kfd2', FALSE)""" %(a, mobil)
# sql = "INSERT INTO T_user_info(user_name, user_mobile, user_password) VALUE (%s, %s, %s)" % (mobile, mobile, passwd)
# sql = "INSERT INTO T_user_info(user_password, user_name, user_mobile) VALUES (\"%s\", \"%s\", \"%s\")" % (mobile, mobile,passwd)
# sql = "INSERT INTO T_user_info(user_name, user_mobile, user_password) VALUES (%s, %s, %s)" % (mobile, mobile, passwd)
# print(sql)
# DBTool.insert(sql)
m = 15

sq = 'UPDATE T_user_info SET '
# if mobile:
#     sq += "user_mobile='%s' "%mobile
# if passwd:
#     sq += "user_password='%s' "%passwd
# if m:
#     sq += "user_age=%d "%m
# sq += "user_update_time='%s' WHERE user_mobile='%s'"%('2017-15-15 15:15:15', mobile)
# print(sq)
# a = None
# b = int(a)
# if b:
#     print(a)
# else:
#     print("a is none")

# update_sql = "UPDATE T_user_info SET user_avatar='%s' WHERE user_id='%s'" %(user_avatar_url, user_id)
# DBTool.excute_sql(sq)


if sq:
    mp = "123"
else:
    mp = "qwe"

print(mp)
mobile = "18273165102"
print("*"*50)
sql = "SELECT * FROM T_user_info WHERE user_mobile=\"%s\"" % mobile

result = DBTool.query_one(sql)  # 查询一个，返回字典
if result == None:
    print("none--")
if result == {}:
    print("--error")
if not result:
    print("not ----")
print(result)
print("*"*50)


# query_sql = "SELECT * FROM T_user_info WHERE user_mobile = (%s)"%(mobil)
# query_sql = "SELECT * FROM T_user_info WHERE user_id > 3"
user_id = None
# query_sql = "SELECT * FROM T_user_info WHERE isnull(user_mobile, '%s')='%s' AND isnull(user_id, %s)=%s" % (mobile, mobile, user_id, user_id)
# print(query_sql)
# query_sql = "SELECT * FROM T_home_data INNER JOIN T_user_info ON home_own_user_id=user_id WHERE home_id > 13"
# result = DBTool.query_all(query_sql)

# print(type(result))
# print(result)
# print(result.get('user_mobile'))
# print(result.get('home_content_text'))
# a = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(a)
# print(type(a))
# print("a=%s"%a)


#
# {
# 	"user_id":23,
# 	"home_content_text":"it's beauteful day",
# 	"home_pic_thumb_urls":["https://imgsa.baidu.com/forum/w%3D580%3B/sign=4ad19f5a3fa85edffa8cfe2b796f0823/9e3df8dcd100baa13bf1b1b14c10b912c9fc2edf.jpg","https://imgsa.baidu.com/forum/w%3D580%3B/sign=4b4fc93a084f78f0800b9afb490a0b55/1e30e924b899a901fcaa0c5816950a7b0308f5c5.jpg"],
# 	"home_pic_original_urls":["https://imgsa.baidu.com/forum/w%3D580%3B/sign=4ad19f5a3fa85edffa8cfe2b796f0823/9e3df8dcd100baa13bf1b1b14c10b912c9fc2edf.jpg","https://imgsa.baidu.com/forum/w%3D580%3B/sign=4b4fc93a084f78f0800b9afb490a0b55/1e30e924b899a901fcaa0c5816950a7b0308f5c5.jpg"],
# 	"home_content_type":2
# }


# class test(object):
#     """test"""
#     @classmethod
#     @tornado.gen.coroutine
#     def addSum(a, b):
#         print('--1')
#         # return a + b
#         raise tornado.gen.Return(a + b)
#
#
#
#     @classmethod
#     @tornado.gen.coroutine
#     def get_return(cls, num):
#         print('--0')
#         a = yield test.addSum(num, 10)
#         print('--2')
#         return a
#         # raise tornado.gen.Return(a)
#
# print('-----')
# kk = test.get_return(12)
# print(kk)




