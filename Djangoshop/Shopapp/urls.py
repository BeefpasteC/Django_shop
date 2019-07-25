from django.urls import path,re_path
from Shopapp.views import *

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('index/', index),
    path('rs/', resgister_store),
    path('ag/', add_goods),
    path('sl/', shop_list),
    path('e4/', error_404),
    re_path(r'^gs/(?P<goods_id>\d+)', goods_summary),
    re_path(r'ug/(?P<goods_id>\d+)', update_goods),
]

