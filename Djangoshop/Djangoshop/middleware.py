#中间件的元类，所有自定义的中间件都是基于当前类型进行重写的
from django.utils.deprecation import MiddlewareMixin
import os
import datetime
from django.http import HttpResponse
from Djangoshop.settings import BASE_DIR
class MiddlewareTest(MiddlewareMixin):
    def process_request(self,request):
        '''
        :param request: 视图没有处理请求
        :return:
        '''
        username = request.GET.get('username')
        if username and username == 'lb':
            return HttpResponse('404')
        print('this is process_request')

    def process_view(self,request,view_func,view_args,view_kwargs):
        '''
        :param request: 视图没有处理请求
        :param view_func:视图函数
        :param view_args:视图函数的参数，元组格式
        :param view_kwargs:视图函数的参数，字典格式
        :return:
        '''
        print('this is process_view')

    def process_exception(self,request,exception):
        '''
        :param request:视图处理中的请求
        :param exception: 错误
        :return:
        '''
        # 报错日志
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = 'Error'
        content = str(exception)
        log_result = '%s [%s] %s'%(now,level,content)
        file_path = os.path.join(BASE_DIR,'error.log')
        with open(file_path,'a') as f:
            f.write(log_result)
        print('this is process_exception')
    def process_template_response(self,request,response):
        '''
        :param request: 视图处理完成的请求
        :param response: 视图处理完的响应
        :return:
        '''

        print('this is process_template_response')
        return response

    def process_response(self,request,response):
        '''
        :param request: 视图处理完成的请求
        :param response: 视图处理完的响应
        :return:
        '''
        response.set_cookie('hhh','111')
        print('this is process_response')
        return response





















