'''
当前文件只是为了规定接口的模型和数据字段
'''

from rest_framework import serializers

from Shopapp.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
    声明查询的表和返回的字段
    '''
    class Meta: # 元类
        model  = Goods #要进行接口序列化的模型
        fields = ['goods_name','goods_price','goods_date','goods_safeDate','id',
                  'goods_number','goods_description'] #序列化要返回的字段


class GoodsTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoodsType
        fields = ['name','description']