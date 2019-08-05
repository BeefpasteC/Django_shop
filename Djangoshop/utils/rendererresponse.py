from rest_framework.renderers import JSONRenderer
class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        '''
        自定义接口返回数据
        :param data: 返回数据
        :param accepted_media_type: 接收的类型
        :param renderer_context: 呈现的内容
        '''
        if renderer_context: #如果有请求的数据过来
            if isinstance(data,dict): #判断返回的数据是否为字典
                msg = data.pop('msg','请求成功') #如果是字典，获取字典当中的msg参数
                code = data.pop('code',0) #如果是字典，获取字典当中的code参数
            else: #非字典类型
                msg = '请求成功'
                code = 0
            ret = {
                'msg': msg,
                'code': code,
                'author': '禹博文',
                'data': data
            } # 重新构建返回的数据格式
            return super().render(ret,accepted_media_type,renderer_context) #返回数据格式
        else:
            return super().render(data,accepted_media_type,renderer_context) #如果没有发生修改，返回原格式

