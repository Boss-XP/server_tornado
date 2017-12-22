# coding: utf-8

from handlers.BaseHandler import RequestBaseHandler
from constants import Res
from dbHandler.DBTools import DBTool
import json

class PublishPPYHandler(RequestBaseHandler):
    """发布数据接口"""
    def post(self, *args, **kwargs):
        user_id = self.json_args.get('user_id')
        ppy_content_text = self.json_args.get('ppy_content_text')
        ppy_content_type = self.json_args.get('ppy_content_type')
        if not all([user_id, ppy_content_text, ppy_content_type]):
            return self.write(dict(code=Res.PARAMERR, msg='参数不全', data={}))

        if ppy_content_type == 2:
            ppy_pic_thumb_urls = self.json_args.get('ppy_pic_thumb_urls')
            ppy_pic_original_urls = self.json_args.get('ppy_pic_original_urls')
            ppy_pic_sizes = self.json_args.get('ppy_pic_sizes')
            if not all([ppy_pic_thumb_urls, ppy_pic_original_urls, ppy_pic_sizes]):
                return self.write(dict(code=Res.PARAMERR, msg='参数不全', data={}))
            # pic_thumb_urls_str = ""
            # for url in ppy_pic_thumb_urls:
            #     pic_thumb_urls_str += url
            #     pic_thumb_urls_str += " ,"
            # pic_original_urls_str = ""
            # for ourl in ppy_pic_original_urls:
            #     pic_original_urls_str += ourl
            #     pic_original_urls_str += " ,"
            # print(json.dumps(ppy_pic_sizes))

            #-------------------------------------------------------如果接收到的是json类型的字符串,转为json保存
            pic_thumb_urls = json.dumps(ppy_pic_thumb_urls)
            pic_thumb_urls = json.dumps(pic_thumb_urls)
            pic_original_urls = json.dumps(ppy_pic_original_urls)
            pic_original_urls = json.dumps(pic_original_urls)
            pic_sizes = json.dumps(ppy_pic_sizes)
            pic_sizes = json.dumps(pic_sizes)

            print(json.dumps(pic_sizes))
            print(pic_original_urls)
            print(pic_sizes)
            listt = ["sdfksadjfkljas"]
            print(listt)
            print(json.dumps(listt))

            sql = """INSERT INTO T_ppy_info (ppy_own_user_id, ppy_content_text, ppy_content_type, ppy_pic_thumb_urls, ppy_pic_original_urls, ppy_pic_sizes) \
                    VALUE (%d, \"%s\", %d, %s, %s, %s)"""%(user_id, ppy_content_text, ppy_content_type, pic_thumb_urls, pic_original_urls, pic_sizes)
            print(sql)
            # return
            # -----------------------------------------------------------------

            # 直接以字符串的方式保存
            # sql = """INSERT INTO T_ppy_info (ppy_own_user_id, ppy_content_text, ppy_content_type, ppy_pic_thumb_urls, ppy_pic_original_urls, ppy_pic_sizes) \
            #                     VALUE (%d, \"%s\", %d, %s, %s, %s)""" % (user_id, ppy_content_text, ppy_content_type, ppy_pic_thumb_urls, ppy_pic_original_urls, ppy_pic_sizes)

        elif ppy_content_type == 3:
            ppy_video_cover_url = self.json_args.get('ppy_video_cover_url')
            ppy_video_url = self.json_args.get('ppy_video_url')
            ppy_video_cover_size = self.json_args.get('ppy_video_cover_size')
            if not all([ppy_video_cover_url, ppy_video_url]):
                return self.write(dict(code=Res.PARAMERR, msg='参数不全', data={}))

            video_cover_size = json.dumps(ppy_video_cover_size)
            video_cover_size = json.dumps(video_cover_size)
            sql = """INSERT INTO T_ppy_info (ppy_own_user_id, ppy_content_text, ppy_content_type, ppy_video_cover_url, ppy_video_url, ppy_video_cover_size) \
                                VALUE (%d, \"%s\", %d, \"%s\", \"%s\", %s)""" % (user_id, ppy_content_text, ppy_content_type, ppy_video_cover_url, ppy_video_url, ppy_video_cover_size)

            # sql = """INSERT INTO T_ppy_info (ppy_own_user_id, ppy_content_text, ppy_content_type, ppy_video_cover_url, ppy_video_url, ppy_video_cover_size) \
            #         VALUE (%d, \"%s\", %d, \"%s\", \"%s\", \"%s\")"""%(user_id, ppy_content_text, ppy_content_type, ppy_video_cover_url, ppy_video_url, ppy_video_cover_size)
        else:
            sql = """INSERT INTO T_ppy_info (ppy_own_user_id, ppy_content_text, ppy_content_type) \
                    VALUE (%d, \"%s\", %d)"""%(user_id, ppy_content_text, ppy_content_type)

        if DBTool.excute_sql(sql):
            return self.write(dict(code=Res.OK, msg='发布成功', data={}))
        else:
            return self.write(dict(code=Res.SERVERERR, msg='发布失败', data={}))



class GetPPYCommentsHandler(RequestBaseHandler):
    """获取ppy评论详情接口"""
    def post(self, *args, **kwargs):
        # user_id = self.json_args.get('user_id')
        ppy_id = self.json_args.get('ppy_id')
        if not ppy_id:
            return self.write(dict(code=Res.PARAMERR, msg='参数不全', data={}))

        sql = """SELECT ppy_comment_id,ppy_comment_text,ppy_comment_time, user_id,user_name, user_avatar,user_vip_level \
         FROM T_ppy_comment_info INNER JOIN T_user_info ON ppy_comment_own_user_id=user_id WHERE ppy_comment_own_ppy_id=%d ORDER BY ppy_comment_time DESC""" % ppy_id


        print(sql)
        results = DBTool.query_all(sql)
        print("------------")
        print(results)
        print(type(results))
        if (type(results) == tuple) and (len(results) == 0):
            return self.write(dict(code=Res.OK, msg='暂无评论', data={}))

        if not results: #过滤掉空列表的情况
            return self.write(dict(code=Res.DBERR, msg='获取评论失败', data={}))

        comments = []
        for result in results:
            comment_time = result.get('ppy_comment_time')
            if not comment_time:
                continue
            result['ppy_comment_time'] = str(comment_time)
            comments.append(result)

        if not comments: #过滤掉组装数据后数据为空的情况
            return self.write(dict(code=Res.DBERR, msg='获取评论失败', data={}))

        return self.write(dict(code=Res.DBERR, msg='获取评论成功', data={"comments": comments}))


class LikePPYHandler(RequestBaseHandler):
    """赞--接口"""
    def post(self, *args, **kwargs):
        # user_id = self.json_args.get('user_id')
        ppy_id = self.json_args.get('ppy_id')

        sql = "SELECT * FROM T_ppy_info WHERE ppy_id=%d" % ppy_id
        ppy_result = DBTool.query_all(sql)
        if not ppy_result:
            return self.write(dict(code=Res.DBERR, msg='操作失败，请重试', data={}))

        sql = "UPDATE T_ppy_info SET ppy_content_likes=ppy_content_likes+1 WHERE ppy_id=%d"%ppy_id
        if DBTool.excute_sql(sql):
            return self.write(dict(code=Res.OK, msg='点赞成功', data={}))

        return self.write(dict(code=Res.DBERR, msg='点赞失败', data={}))

class HatePPYHandler(RequestBaseHandler):
    """踩--接口"""
    def post(self, *args, **kwargs):
        ppy_id = self.json_args.get('ppy_id')

        sql = "SELECT * FROM T_ppy_info WHERE ppy_id=%d" % ppy_id
        ppy_result = DBTool.query_all(sql)
        if not ppy_result:
            return self.write(dict(code=Res.DBERR, msg='操作失败，请重试', data={}))

        sql = "UPDATE T_ppy_info SET ppy_content_dislikes=ppy_content_dislikes+1 WHERE ppy_id=%d"%ppy_id
        if DBTool.excute_sql(sql):
            return self.write(dict(code=Res.OK, msg='踩他成功', data={}))

        return self.write(dict(code=Res.DBERR, msg='踩他失败', data={}))


class SharePPYHandler(RequestBaseHandler):
    """分享--接口"""
    def post(self, *args, **kwargs):
        ppy_id = self.json_args.get('ppy_id')

        sql = "SELECT * FROM T_ppy_info WHERE ppy_id=%d" % ppy_id
        ppy_result = DBTool.query_all(sql)
        if not ppy_result:
            return self.write(dict(code=Res.DBERR, msg='操作失败，请重试', data={}))

        sql = "UPDATE T_ppy_info SET ppy_content_share=ppy_content_share+1 WHERE ppy_id=%d" % ppy_id
        if DBTool.excute_sql(sql):
            return self.write(dict(code=Res.OK, msg='分享成功+1', data={}))

        return self.write(dict(code=Res.DBERR, msg='分享计数失败', data={}))


class CommentPPYHandler(RequestBaseHandler):
    """评论--接口"""
    def post(self, *args, **kwargs):
        user_id = self.json_args.get('user_id')
        ppy_id = self.json_args.get('ppy_id')
        comment_text = self.json_args.get('comment_text')
        if not all([user_id, ppy_id, comment_text]):
            return self.write(dict(code=Res.PARAMERR, msg='参数不全', data={}))

        # 查询要评论的ppy和该用户是否存在，理论上不存在的时候不可能进入到评论界面调用评论接口，所以报错提示"操作失败，请重试"
        sql = "SELECT * FROM T_ppy_info WHERE ppy_id=%d" % ppy_id
        ppy_result = DBTool.query_all(sql)
        if not ppy_result:
            return self.write(dict(code=Res.DBERR, msg='操作失败，请重试', data={}))

        sql = "SELECT * FROM T_user_info WHERE user_id=%d" % user_id
        user_result = DBTool.query_all(sql)
        if not user_result:
            return self.write(dict(code=Res.DBERR, msg='操作失败，请重试', data={}))

        sql = "INSERT INTO T_ppy_comment_info (ppy_comment_own_user_id,ppy_comment_own_ppy_id,ppy_comment_text) VALUE (%d, %d, \"%s\")"%(user_id, ppy_id, comment_text)
        if DBTool.excute_sql(sql):
            sql = "UPDATE T_ppy_info SET ppy_content_comments=ppy_content_comments+1 WHERE ppy_id=%d" % ppy_id
            if DBTool.excute_sql(sql): #评论计数加1成功
                pass

            return self.write(dict(code=Res.OK, msg='评论成功', data={}))

        return self.write(dict(code=Res.DBERR, msg='评论失败', data={}))
