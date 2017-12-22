# coding:utf-8

import handlers.IndexHandler
import handlers.FaviconHandler
import handlers.TestHandler
# import handlers.AccountHandler
# import handlers.HomeHandler
# import handlers.PublishHandler

from handlers import AccountHandler,HomeHandler,PPYHandler

import handlers.StaticFileHandler

urls_hander = [

    (r"^/api/account/get_verify_code",AccountHandler.GetVerifyCodeHandler),
    (r"^/api/account/register$",AccountHandler.RegisterHandler),
    (r"^/api/account/login$",AccountHandler.LoginHandler),
    (r"^/api/account/get_userinfo$",AccountHandler.GetUserInfo),

    (r"^/api/home/get_home_data$",HomeHandler.GetHomeData),
    (r"^/api/ppy/publish_ppy$", PPYHandler.PublishPPYHandler),
    (r"^/api/ppy/get_ppy_comments$", PPYHandler.GetPPYCommentsHandler),
    (r"^/api/ppy/comment_ppy$", PPYHandler.CommentPPYHandler),

    # 赞踩转接口，完全可以用一个，数据中加一个字段注明即可--下一步优化
    (r"^/api/ppy/like_ppy$", PPYHandler.LikePPYHandler),
    (r"^/api/ppy/hate_ppy$", PPYHandler.HatePPYHandler),
    (r"^/api/ppy/share_ppy$", PPYHandler.SharePPYHandler),


    (r"^/api/test$", handlers.TestHandler.TestHandler),
    (r"^/favicon.ico$",handlers.FaviconHandler.GetFavicon),

    (r"^/css/(\w){1,}.css$", handlers.StaticFileHandler.CssHandler),
    (r"^/images/(\w){1,}.png$", handlers.StaticFileHandler.ImageHandler),

    (r"^/*$", handlers.IndexHandler.IndexHandler),

]