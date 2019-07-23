import hashlib

from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from Shopapp.models import *

# Create your views here.
# 密码加密
def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    response = md5.hexdigest()
    return response


# 注册
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        nickname = request.POST.get('nickname')
        if username and password:
            seller = Seller()
            seller.username = username
            seller.password = set_password(password)
            seller.nickname = nickname
            seller.save()
            return HttpResponseRedirect('/shop/login/')
    return render(request,'shopapp/register.html')

# cookie值校验登录
def cook_session(fun):

    def inner(request,*args,**kwargs):
        cookie_data = request.COOKIES.get('username')
        session_data = request.session.get('username')
        if cookie_data and session_data:
            user = Seller.objects.filter(username=cookie_data).first()
            if user and session_data == cookie_data:
                return fun(request,*args,**kwargs)
        return HttpResponseRedirect('/shop/login/')
    return  inner


# 登录
def login(request):

    response = render(request,'shopapp/login.html') #如果从登录页加载，
    response.set_cookie("login_from","login_page") # 获得cookie值

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password :
            user = Seller.objects.filter(username = username).first()
            if user :
                web_password = set_password(password)
                cookies = request.COOKIES.get("login_from")
                if user.password == web_password and cookies == 'login_page':
                    response = HttpResponseRedirect('/shop/index/')
                    response.set_cookie('username',username)
                    response.set_cookie('user_id',user.id) #cookie提供用户id方便其他功能查询
                    request.session['username'] = username
                    return response
    return response


# 首页
@ cook_session
def index(request):
    '''
    检查店铺是否有逻辑
    :param request:
    :return:
    '''
    # 查询当前用户
    user_id = request.COOKIES.get('user_id')
    if user_id:
        user_id = int(user_id)
    else:
        user_id = 0
    # 通过用户查询店铺是否存在（店铺和用户的id进行关联）
    store = Store.objects.filter(user_id=user_id).first()
    if store:
        is_store = 1
    else:
        is_store = 0
    return render(request,'shopapp/index.html',{'is_store':is_store})

# 店铺注册
def resgister_store(request):
    type_list = StoreType.objects.all()
    if request.method == 'POST':
        post_data = request.POST # 接收post数据
        store_name = post_data.get('store_name')
        store_description = post_data.get('store_description')
        store_phone = post_data.get('store_phone')
        store_money = post_data.get('store_money')
        store_address = post_data.get('store_address')

        user_id = int(request.COOKIES.get('user_id')) #通过cookie，来得到user_id
        type_list = post_data.get('type')#通过request.post得到类型，但是是一个列表
        store_logo = request.FILES.get('store_logo')#通过request.Files得到

        #保存非多对多数据
        store = Store()
        store.store_name =store_name
        store.store_descripton = store_description
        store.store_phone = store_phone
        store.store_money = store_money
        store.store_address = store_address
        store.user_id = user_id
        store.store_logo = store_logo #django1.8之后图片可以直接保存
        store.save() #保存。生成数据库当中的一条数据
        # 在生成的数据当中添加多对多字段。
        for i in type_list: #循环type列表，得到类型id
            store_type = StoreType.objects.get(id=i) # 查询类型数据
            store.type.add(store_type) #添加到类型字段，多对多的映射表
        store.save() # 保存数据


    return render(request,'shopapp/resgister_store.html',locals())


# 添加商品
def add_goods(request):
    """
    负责添加商品
    """
    if request.method == "POST":
        #获取post请求
        goods_name = request.POST.get("goods_name")
        goods_price = request.POST.get("goods_price")
        goods_number = request.POST.get("goods_number")
        goods_description = request.POST.get("goods_description")
        goods_date = request.POST.get("goods_date")
        goods_safeDate = request.POST.get("goods_safeDate")
        goods_store = request.POST.get("goods_store")
        goods_image = request.FILES.get("goods_image")
        #开始保存数据
        goods = Goods()
        goods.goods_name = goods_name
        goods.goods_price = goods_price
        goods.goods_number = goods_number
        goods.goods_description = goods_description
        goods.goods_date = goods_date
        goods.goods_safeDate = goods_safeDate
        goods.goods_image = goods_image
        goods.save()
        #保存多对多数据
        goods.store_id.add(
            Store.objects.get(id = int(goods_store))
        )
        goods.save()
        return HttpResponseRedirect("/shop/sl/")
    return render(request,"shopapp/add_goods.html")

# 商品列表
def shop_list(request):
    """
    商品的列表页
    :param request:
    :return:
    """
    #获取两个关键字
    keywords = request.GET.get("keywords","") #查询关键词
    page_num = request.GET.get("page_num",1) #页码
    if keywords: #判断关键词是否存在
        goods_list = Goods.objects.filter(goods_name__contains=keywords)#完成了模糊查询
    else: #如果关键词不存在，查询所有
        goods_list = Goods.objects.all()
    #分页，每页3条
    paginator = Paginator(goods_list,3)
    page = paginator.page(int(page_num))
    page_range = paginator.page_range
    #返回分页数据
    return render(request,"shopapp/shop_list.html",{"page":page,"page_range":page_range,"keywords":keywords})