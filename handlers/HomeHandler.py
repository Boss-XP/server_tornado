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

        if (not begin_index and begin_index != 0) or (not count):
            return self.write(dict(code=Res.PARAMERR, msg='参数不全', data={}))

        sql = """SELECT user_id, user_name, user_avatar, user_vip_level, \
            ppy_id, ppy_publish_time, ppy_content_text, ppy_content_type, ppy_pic_thumb_urls, ppy_pic_original_urls, ppy_pic_sizes, ppy_video_cover_url, ppy_video_url, ppy_video_cover_size, \
            ppy_content_likes, ppy_content_dislikes, ppy_content_share, ppy_content_comments \
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
            else:
                del result['ppy_video_cover_url']
                del result['ppy_video_url']
                del result['ppy_video_cover_size']
                del result['ppy_pic_thumb_urls']
                del result['ppy_pic_original_urls']
                del result['ppy_pic_sizes']
                obj = ["dsfflaksjdflkajsdlkf"]

            result['ppy_publish_time'] = str(ppy_publish_time)
            res_data.append(result)

        if not res_data:
            return self.write(dict(code=Res.DBERR, msg='获取主页数据失败', data={}))

        return self.write(dict(code=Res.OK, msg='获取数据成功', data=res_data))