from django.urls import path,re_path
from Buyerapp.views import *

urlpatterns = [
    path('login/',login),  # 登录
    path('register/',register), # 注册账号
    path('index/',index),  # 首页
    path('logout/',logout),  # 退出
    path('gl/',goods_list),  # 商品列表
    path('pr/',pay_result),  # 支付结果
    path('po/',pay_order),  # 支付
    path('uc/',user_center),  # 用户中心
    path('ol/',order_list),  # 我的订单
    path('sc/',shopping_cart),  # 购物车
    path('ac/',add_cart),  # 添加到购物车
    path('so/',submit_order),  # 提交订单
    path('gd/',goods_description),  # 商品详情
    path('ra/',receive_adress),  # 收货地址

]

urlpatterns += [
    path('base/',base)

]
