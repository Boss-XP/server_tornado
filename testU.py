# coding:utf-8

# import dbHandler.DBTools
from dbHandler.DBTools import DBTool
import datetime
import tornado
import tornado.gen
import json



# dbHandler.DBTools.DBTool

resul = {}
if not resul:
    print("---")
else:
    print("xppp")

# 添加一个用户
# mobile = "18272165102"
# passwd = "jkfdsjaksdf"

# sql = """INSERT INTO T_user_info(\
#           user_name, user_password, user_gender, user_age, user_mobile, user_avatar, user_isdeleted) \
#           VALUE ('bxp4', '1233212', %d, 122, %s, 'kfd2', FALSE)""" %(a, mobil)
# sql = "INSERT INTO T_user_info(user_name, user_mobile, user_password) VALUE (%s, %s, %s)" % (mobile, mobile, passwd)
# sql = "INSERT INTO T_user_info(user_password, user_name, user_mobile) VALUES (\"%s\", \"%s\", \"%s\")" % (mobile, mobile,passwd)
# sql = "INSERT INTO T_user_info(user_name, user_mobile, user_password) VALUES (%s, %s, %s)" % (mobile, mobile, passwd)
# print(sql)
# DBTool.insert(sql)


# 点赞表插入同时更新ppy_info表的like字段
sq = "INSERT INTO T_ppy_like_users (ppy_id, ppy_like_user_id) VALUE(10, 20)"
sql2 = "UPDATE T_ppy_info SET ppy_content_likes=ppy_content_likes+1 WHERE ppy_id>1000"
if DBTool.excute_sqls([sq, sql2]):
    print("操作--OK")
else:
    print("操作--Failed")



# 从ppy_info表中查出所有的数据
# seletSql = "SELECT * FROM T_ppy_info"
# results = DBTool.query_all(seletSql)
# # print(results)
# for r in results:
#     ptype = r['ppy_content_type']
#     if ptype == 2:
#         picss = r.get('ppy_pic_thumb_urls')
#         print(picss)
#         picss2 = json.load(picss)
#         print(type(picss2))





# query_sql = "SELECT * FROM T_user_info WHERE user_mobile = (%s)"%(mobil)
# query_sql = "SELECT * FROM T_user_info WHERE user_id > 3"
# user_id = None
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




