from enum import Enum


# 用户分类(层级菜单(新浪微博,个人与公司)) 普通用户(vip,好友,同学,亲人,同事,商业伙伴,反馈者),公司(我的公司,伙伴公司),组织,团体, 陌生(其他,非通过,类似邮件消息)

class UserType(Enum):
    normal = 1
    company = 2
    organization = 4
    group = 8
    strange = 16
