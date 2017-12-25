# coding: utf-8

from handlers.BaseHandler import RequestBaseHandler
from constants import Res
from dbHandler.DBTools import DBTool
import json

class GetHomeData(RequestBaseHandler):
    """首页获取数据接口--分页查询"""
    def post(self, *args, **kwargs):
        begin_index = self.json_args.get('begin_index')
        count = self.json_args.get('count')
        user_id = self.json_args.get('user_id')

        if (not begin_index and begin_index != 0) or (not count):
            return self.write(dict(code=Res.PARAMERR, msg='参数不全', data={}))

        sql = """SELECT user_id, user_name, user_avatar, user_vip_level, \
            ppy_id, ppy_publish_time, ppy_content_text, ppy_content_type, ppy_pic_thumb_urls, ppy_pic_original_urls, ppy_pic_sizes, ppy_video_cover_url, ppy_video_url, ppy_video_cover_size, \
            ppy_content_likes, ppy_content_hates, ppy_content_share, ppy_content_comments \
            FROM T_ppy_info INNER JOIN T_user_info ON ppy_own_user_id=user_id WHERE ppy_id > %d ORDER BY ppy_publish_time DESC LIMIT %d"""\
              %(begin_index, count)
        results = DBTool.query_all(sql)

        if (type(results) == tuple) and (len(results) == 0):
            return self.write(dict(code=Res.OK, msg='暂无ppy数据', data={}))

        if not results:  # 过滤掉空列表的情况，即查询数据库失败的情况
            return self.write(dict(code=Res.DBERR, msg='获取主页数据失败', data={}))

        res_data = []
        for result in results:
            if (not result) or (type(result) != dict):
                continue
            # user_name = result.get('user_name', '')
            # user_id = result.get('user_id')
            # user_avatar = result.get('user_name', '')

            ppy_content_type = result.get('ppy_content_type')
            ppy_publish_time = result.get('ppy_publish_time')
            if not all([ppy_content_type, ppy_publish_time]):
                continue

            # 图片
            if ppy_content_type == 2 :
                # 删掉视频类空数据
                del result['ppy_video_cover_url']
                del result['ppy_video_url']
                del result['ppy_video_cover_size']

                ppy_pic_thumb_urls = result.get('ppy_pic_thumb_urls')
                ppy_pic_original_urls = result.get('ppy_pic_original_urls')
                ppy_pic_sizes = result.get('ppy_pic_sizes')

                if not all([ppy_pic_original_urls, ppy_pic_thumb_urls, ppy_pic_sizes]):
                    continue
                pic_thumb_urls = json.loads(ppy_pic_thumb_urls)
                pic_urls = json.loads(ppy_pic_original_urls)
                pic_sizes = json.loads(ppy_pic_sizes)
                if not all([pic_thumb_urls, pic_thumb_urls, pic_sizes]):
                    continue
                result['ppy_pic_thumb_urls'] = pic_thumb_urls
                result['ppy_pic_original_urls'] = pic_urls
                result['ppy_pic_sizes'] = pic_sizes

                # ppy_pic_thumb_urls_list = ppy_pic_thumb_urls.strip(',').split(' ,')
                # ppy_pic_original_urls_list = ppy_pic_original_urls.strip(',').split(' ,')
                # result['ppy_pic_thumb_urls'] = ppy_pic_thumb_urls_list
                # result['ppy_pic_original_urls'] = ppy_pic_original_urls_list
            # 视频
            elif ppy_content_type == 3:
                del result['ppy_pic_thumb_urls']
                del result['ppy_pic_original_urls']
                del result['ppy_pic_sizes']
                ppy_video_cover = result.get('ppy_video_cover_url')
                ppy_video_path = result.get('ppy_video_url')
                ppy_video_cover_size = result.get('ppy_video_cover_size')
                if not all([ppy_video_cover, ppy_video_path, ppy_video_cover_size]):
                    continue
                video_cover_size = json.loads(ppy_video_cover_size)
                if not video_cover_size:
                    continue
                result['ppy_video_cover_size'] = video_cover_size
            else:
                del result['ppy_video_cover_url']
                del result['ppy_video_url']
                del result['ppy_video_cover_size']
                del result['ppy_pic_thumb_urls']
                del result['ppy_pic_original_urls']
                del result['ppy_pic_sizes']

            result['ppy_is_liked'] = False
            result['ppy_is_hated'] = False
            # result['ppy_is_shared'] = False
            # result['ppy_is_comment'] = False

            result['ppy_publish_time'] = str(ppy_publish_time)
            res_data.append(result)

        if not res_data:
            return self.write(dict(code=Res.DBERR, msg='获取主页数据失败', data={}))

        if user_id:
            print(user_id)
            like_sql = "SELECT ppy_id FROM T_ppy_like_users WHERE ppy_like_user_id=%d"%user_id
            like_ppy_id_results = DBTool.query_all(like_sql)

            hate_sql = "SELECT ppy_id FROM T_ppy_hate_users WHERE ppy_hate_user_id=%d"%user_id
            hate_ppy_id_results = DBTool.query_all(hate_sql)

            if len(like_ppy_id_results) > 0 or len(hate_ppy_id_results) > 0:
                print('----------xp----------------result---')
                print(like_ppy_id_results)
                print(hate_ppy_id_results)
                for result in res_data:
                    ppy_id = result.get('ppy_id')
                    like_count = result.get('ppy_content_likes')
                    hate_count = result.get('ppy_content_hates')
                    if like_ppy_id_results.__contains__({"ppy_id":ppy_id}) and like_count > 0:
                        result['ppy_is_liked'] = True
                        continue
                    if hate_ppy_id_results.__contains__({"ppy_id":ppy_id}) and hate_count > 0:
                        result['ppy_is_hated'] = True
            # print('----------xp----------------result---')
            # print(res_data)
        #
        #     share_sql = "SELECT ppy_id FROM T_ppy_share_users WHERE user_id=%d" % user_id
        #     share_ppy_id_results = DBTool.query_all(share_sql)
        #
        #     comment_sql = "SELECT ppy_id FROM T_ppy_comment_users WHERE user_id=%d" % user_id
        #     comment_ppy_id_results = DBTool.query_all(comment_sql)
        #     if len(like_ppy_id_results) > 0:
        #         for result in res_data:
        #             ppy_id = result.get('ppy_id')
        #             if like_ppy_id_results.__contains__(ppy_id):
        #                 result['ppy_is_liked'] = True


        return self.write(dict(code=Res.OK, msg='获取数据成功', data=res_data))