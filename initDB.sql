CREATE DATABASE IF NOT EXISTS iHome DEFAULT CHARSET=utf8;

USE iHome;

CREATE TABLE IF NOT EXISTS T_user_info(
  user_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY COMMENT '用户id',
  user_name VARCHAR(64) NOT NULL DEFAULT "" COMMENT '用户名',
  user_password VARCHAR(128) NULL DEFAULT '' COMMENT 'password',
  user_token VARCHAR(128) NULL COMMENT 'token',

  user_mobile CHAR(11) NOT NULL DEFAULT '' COMMENT 'mobile phone',
  user_avatar VARCHAR(256) NULL COMMENT 'user avatar url',

  user_gender TINYINT NULL DEFAULT 0 COMMENT '用户性别',
  user_age TINYINT NULL COMMENT '用户年龄',
  user_real_name VARCHAR(64) NULL COMMENT '用户真实姓名',
  user_birthday DATETIME NULL COMMENT '用户生日',
  user_area VARCHAR(128) NULL COMMENT '用户所在地',

  user_create_time DATETIME DEFAULT current_timestamp COMMENT 'create time',
  user_update_time DATETIME DEFAULT current_timestamp COMMENT 'update time',

  user_isdeleted BOOL NOT NULL DEFAULT FALSE COMMENT '是否注销',
  user_level TINYINT NOT NULL DEFAULT 0 COMMENT '用户等级',
  user_vip_level TINYINT NOT NULL DEFAULT 0 COMMENT '用户VIP等级',
  user_profil VARCHAR(128) NULL COMMENT '用户简介',

  UNIQUE (user_mobile),
  UNIQUE (user_name),
  KEY (user_name)

) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT 'table off user info';

#
# CREATE TABLE IF NOT EXISTS T_home_data(
#   home_own_user_id BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '内容所属用户id',
#   home_id BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '内容ID',
#   home_publish_time DATETIME NOT NULL DEFAULT current_timestamp COMMENT '发布时间',
#   home_content_text VARCHAR(128) DEFAULT "" COMMENT '内容主体',
#
#   home_content_type INT UNSIGNED NOT NULL DEFAULT 1 COMMENT '内容类型，1-纯文本，2-图片，3-视频',
#
#   home_pic_thumb_urls TEXT NULL COMMENT '图片内容的缩略图',
#   home_pic_original_urls TEXT NULL COMMENT '图片原始图',
#
#   home_video_cover_url VARCHAR(256) NULL COMMENT '视频封面图地址',
#   home_video_url VARCHAR(256) NULL COMMENT '视频地址',
#
#   home_content_likes INT UNSIGNED DEFAULT 0 COMMENT '赞数',
#   home_content_dislikes INT UNSIGNED DEFAULT 0 COMMENT '踩数',
#   home_content_share INT UNSIGNED DEFAULT 0 COMMENT '转数',
#   home_content_comments INT UNSIGNED DEFAULT 0 COMMENT '评数',
#
#   CONSTRAINT FOREIGN KEY (home_own_user_id) REFERENCES  T_user_info(user_id)
# )ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT '首页每一则内容数据表';
# # engine = create_engine('mysql://scrat:'+'scratdb123'+"@{}/{}?charset=utf8".format(DB_ADDRESS,stockdb),encoding='utf-8');
#
#
#
# CREATE TABLE IF NOT EXISTS T_home_content_comments(
#   comment_own_user_id BIGINT UNSIGNED NOT NULL COMMENT '评论用户id',
#   comment_own_conten_id BIGINT UNSIGNED NOT NULL COMMENT '被评论的内容id',
#
#   comment_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT COMMENT '评论id',
#   comment_text VARCHAR(128) NOT NULL DEFAULT '' COMMENT '评论内容',
#   comment_time DATETIME NOT NULL DEFAULT current_timestamp COMMENT '评论时间',
#
#
#   CONSTRAINT FOREIGN KEY (comment_own_user_id)REFERENCES T_user_info(user_id),
#   CONSTRAINT FOREIGN KEY (comment_own_conten_id) REFERENCES T_home_data(home_id)
# ) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT '首页每一则内容的评论数据表';
#



CREATE TABLE IF NOT EXISTS T_ppy_info(
  ppy_own_user_id BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '内容所属用户id',
  ppy_id BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '内容ID',
  ppy_publish_time DATETIME NOT NULL DEFAULT current_timestamp COMMENT '发布时间',
  ppy_content_text VARCHAR(128) DEFAULT "" COMMENT '内容主体',

  ppy_content_type INT UNSIGNED NOT NULL DEFAULT 1 COMMENT '内容类型，1-纯文本，2-图片，3-视频',

  ppy_pic_thumb_urls JSON NULL COMMENT '图片内容的缩略图json数据',
  ppy_pic_original_urls JSON NULL COMMENT '图片原始图json数据',
  ppy_pic_sizes JSON NULL COMMENT '图片的尺寸json数据',

  ppy_video_cover_url VARCHAR(256) NULL COMMENT '视频封面图地址',
  ppy_video_url VARCHAR(256) NULL COMMENT '视频地址',
  ppy_video_cover_size JSON NULL COMMENT '视频封面图片的尺寸json数据',

  ppy_content_likes INT UNSIGNED DEFAULT 0 COMMENT '赞数',
  ppy_content_dislikes INT UNSIGNED DEFAULT 0 COMMENT '踩数',
  ppy_content_share INT UNSIGNED DEFAULT 0 COMMENT '转数',
  ppy_content_comments INT UNSIGNED DEFAULT 0 COMMENT '评数',

  CONSTRAINT FOREIGN KEY (ppy_own_user_id) REFERENCES  T_user_info(user_id)
)ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT '首页每一则内容数据表';
# engine = create_engine('mysql://scrat:'+'scratdb123'+"@{}/{}?charset=utf8".format(DB_ADDRESS,stockdb),encoding='utf-8');



CREATE TABLE IF NOT EXISTS T_ppy_comment_info(
  ppy_comment_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT COMMENT '评论id',

  ppy_comment_own_user_id BIGINT UNSIGNED NOT NULL COMMENT '评论用户id',
  ppy_id BIGINT UNSIGNED NOT NULL COMMENT '被评论的内容id',

  ppy_comment_text VARCHAR(128) NOT NULL DEFAULT '' COMMENT '评论内容',
  ppy_comment_time DATETIME NOT NULL DEFAULT current_timestamp COMMENT '评论时间',


  CONSTRAINT FOREIGN KEY (ppy_comment_own_user_id)REFERENCES T_user_info(user_id),
  CONSTRAINT FOREIGN KEY (ppy_id) REFERENCES T_ppy_info(ppy_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT '首页每一则内容的评论数据表';


CREATE TABLE IF NOT EXISTS T_ppy_like_users(
  ppy_like_user_id BIGINT UNSIGNED NOT NULL COMMENT '用户id',
  ppy_id BIGINT UNSIGNED NOT NULL COMMENT 'ppy id',

#   下面两个外检约束保证增加或者更新数据时,ppy_id 和 user_id有值,即ppy和User要真实存在
  CONSTRAINT FOREIGN KEY (ppy_like_user_id)REFERENCES T_user_info(user_id),
  CONSTRAINT FOREIGN KEY (ppy_id) REFERENCES T_ppy_info(ppy_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT '首页每一则内容的点赞表';

CREATE TABLE IF NOT EXISTS T_ppy_hate_users(
  ppy_hate_user_id BIGINT UNSIGNED NOT NULL COMMENT '用户id',
  ppy_id BIGINT UNSIGNED NOT NULL COMMENT 'ppy id',

  CONSTRAINT FOREIGN KEY (ppy_hate_user_id)REFERENCES T_user_info(user_id),
  CONSTRAINT FOREIGN KEY (ppy_id) REFERENCES T_ppy_info(ppy_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT '首页每一则内容的点赞表';

CREATE TABLE IF NOT EXISTS T_ppy_share_users(
  ppy_share_user_id BIGINT UNSIGNED NOT NULL COMMENT '用户id',
  ppy_id BIGINT UNSIGNED NOT NULL COMMENT 'ppy id',

  CONSTRAINT FOREIGN KEY (ppy_share_user_id)REFERENCES T_user_info(user_id),
  CONSTRAINT FOREIGN KEY (ppy_id) REFERENCES T_ppy_info(ppy_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT '首页每一则内容的点赞表';



#
# CREATE TABLE IF NOT EXISTS T_book_info (
#   book_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY COMMENT 'book id',
#
#   book_content TEXT NOT NULL COMMENT 'book content',
#
#   CONSTRAINT FOREIGN KEY (book_id) REFERENCES  T_user_info(user_id)
# ) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT 'table off book info';
#
# INSERT INTO T_user_info(user_id, user_name, user_password, user_gender, user_age, user_mobile, user_avatar, user_isdeleted) VALUES
#   (1, 'bxp', '123321', 1, 12, '12345678901', 'kfd', FALSE),
#   (2, 'bxp2', '1233212', 1, 12, '12345678902', 'kfd2', FALSE),
#   (3, 'bxp3', '1233213', 1, 12, '12345678903', 'kfd3', FALSE),
#   (4, 'bxp4', '1233214', 1, 12, '12345678904', 'kfd4', FALSE);


# 1. 执行sql文件，在命令行中输入以下(不进入mysql)
# mysql -uroot -p < /Users/xiangpan/Desktop/python_projs/tornado_proj2/initDB.sql
# 2.进入mysql
# mysql -uroot -p
# 3.显示所有的数据库，注意后面都有个s
# show databases;
# 4.进入(使用)某个数据库
# use 数据库名称;
# 5.显示所有的表
# show tables;



