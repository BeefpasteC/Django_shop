from django.urls import path
from Shopapp.views import *

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('index/', index),
    path('rs/', resgister_store),
    path('ag/', add_goods),
    path('sl/', shop_list),
]

