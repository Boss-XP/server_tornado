# coding:utf-8
import pymysql
import logging
import config

class DBTool():
    """数据库工具类"""

    @classmethod
    def insert(DBtool, sql):
        # 打开数据库连接
        db = pymysql.connect(**config.mysql_options)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        is_succeed = True
        # SQL 插入语句
        try:
            # 执行sql语句
            resul = cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print("insert-----------------")
            print(resul)
            print(type(resul))
        except:
            # 如果发生错误则回滚
            db.rollback()
            is_succeed = False
            print("insert-error--------")

        # finally:
        #     db.close()

        # 关闭数据库连接
        db.close()

        return is_succeed


    def updata(sql):
        # 打开数据库连接
        db = pymysql.connect(**config.mysql_options)

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        is_succeed = True

        # SQL 更新语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
            is_succeed = False

        # 关闭数据库连接
        db.close()

        return is_succeed

    def delete(sql):
        # 打开数据库连接
        db = pymysql.connect(**config.mysql_options)

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        is_succeed = True

        # SQL 删除语句

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
            is_succeed = False

        # 关闭连接
        db.close()

        return is_succeed

    @classmethod
    def excute_sql(DBTool, sql):
        print(sql)

        # 打开数据库连接
        db = pymysql.connect(**config.mysql_options)

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        is_succeed = True

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
        except Exception as e:
            # 发生错误时回滚
            db.rollback()
            is_succeed = False
            logging.error(e)

        # 关闭连接
        db.close()

        return is_succeed

    @classmethod
    def query_one(DBTool, sql):
        # 打开数据库连接
        db = pymysql.connect(**config.mysql_options)

        # 使用cursor()方法获取操作游标
        # cursor = db.cursor()
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

        # SQL 查询语句

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchone()
            print(type(results))
        except:
            print("Error: unable to fetch data")
            results = {}

        # 关闭数据库连接
        db.close()

        return results

    @classmethod
    def query_all(DBTool, sql):
        # 打开数据库连接
        db = pymysql.connect(**config.mysql_options)

        # 使用cursor()方法获取操作游标
        # cursor = db.cursor() #返回的数据为元祖或者多层元祖
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor) #返回的数据最底层为字典，上层为列表

        # SQL 查询语句

        try:

            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()

        except:
            print("Error: unable to fetch data")
            results = [] #查询失败，返回空列表

        # 关闭数据库连接
        db.close()

        # 查询结构为0条时，返回数据为空元祖tuple
        return results

