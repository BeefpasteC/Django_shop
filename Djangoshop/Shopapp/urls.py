from django.urls import path,re_path
from Shopapp.views import *




urlpatterns = [
    path('register/', register),# 注册
    path('login/', login),#登录
    path('index/', index),#首页
    path('rs/', resgister_store),#注册店铺
    path('ag/', add_goods),#添加商品
    re_path(r'sl/(?P<state>\w+)', shop_list),# 商品列表
    path('e4/', error_404),#
    re_path(r'^gs/(?P<goods_id>\d+)', goods_summary),# 商品分类
    re_path(r'ug/(?P<goods_id>\d+)', update_goods),# 商品详情
    re_path(r'sg/(?P<state>\w+)/', set_goods),# 商品上下架
    path('gt/', goods_type),# 商品类型
    path('ol/', order_list),# 订单

    path('dgt/', delete_goods_types),# 删除商品类型
    path('gts/', goods_type_summary),# 商品类型分类
]

urlpatterns += [
    path('agl/',ajax_goods_list), # vue 接口测试
    path('ga/',get_add), #celery
    path('swv/',small_white_views), #中间件测试
    path('str/',small_template_response), #中间件测试
]
