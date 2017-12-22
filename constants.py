# coding:utf-8

PIC_CODE_EXPIRES_SECONDS = 180 # 图片验证码的有效期，单位秒
SMS_CODE_EXPIRES_SECONDS = 300 # 图片验证码的有效期，单位秒

SESSION_EXPIRES_SECONDS = 86400 # session数据有效期， 单位秒

QINIU_URL_PREFIX = "http://o91qujnqh.bkt.clouddn.com/" # 七牛存储空间的域名

REDIS_AREA_INFO_EXPIRES_SECONDES = 86400 # redis缓存城区信息的有效期
REDIS_HOUSE_INFO_EXPIRES_SECONDES = 86400 # redis缓存房屋信息的有效期

HOME_PAGE_MAX_HOUSES = 5 # 主页房屋展示最大数量
HOME_PAGE_DATA_REDIS_EXPIRE_SECOND = 7200 # 主页缓存数据过期时间 秒

HOUSE_LIST_PAGE_CAPACITY = 3 # 房源列表页每页显示房屋数目
HOUSE_LIST_PAGE_CACHE_NUM = 2 # 房源列表页每次缓存页面书

REDIS_HOUSE_LIST_EXPIRES_SECONDS = 7200 # 列表页数据缓存时间 秒



class Res:
    OK                  = 0
    DBERR               = 4001
    NODATA              = 4002
    DATAEXIST           = 4003
    DATAERR             = 4004
    SESSIONERR          = 4101
    LOGINERR            = 4102
    PARAMERR            = 4103
    USERERR             = 4104
    ROLEERR             = 4105
    PWDERR              = 4106
    REQERR              = 4201
    IPERR               = 4202
    THIRDERR            = 4301
    IOERR               = 4302
    SERVERERR           = 4500
    UNKOWNERR           = 4501

error_map = {
    Res.OK                    : u"成功",
    Res.DBERR                 : u"数据库查询错误",
    Res.NODATA                : u"无数据",
    Res.DATAEXIST             : u"数据已存在",
    Res.DATAERR               : u"数据错误",
    Res.SESSIONERR            : u"用户未登录",
    Res.LOGINERR              : u"用户登录失败",
    Res.PARAMERR              : u"参数错误",
    Res.USERERR               : u"用户不存在或未激活",
    Res.ROLEERR               : u"用户身份错误",
    Res.PWDERR                : u"密码错误",
    Res.REQERR                : u"非法请求或请求次数受限",
    Res.IPERR                 : u"IP受限",
    Res.THIRDERR              : u"第三方系统错误",
    Res.IOERR                 : u"文件读写错误",
    Res.SERVERERR             : u"内部错误",
    Res.UNKOWNERR             : u"未知错误",
}
