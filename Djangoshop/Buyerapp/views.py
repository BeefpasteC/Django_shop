import hashlib
import time
from alipay import AliPay
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect

from Buyerapp.models import *
from Shopapp.models import *
from Shopapp.views import set_password

# Create your views here.

def base(request):

    return render(request,'buyerapp/base.html')
# cookie校验
def loginValid(fun):
    def inner(request,*args,**kwargs):
        c_user = request.COOKIES.get('username')
        s_user = request.session.get('username')
        if c_user and  s_user and c_user == s_user:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/buyer/login/')
    return inner

# 登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        if username and password:
            user = Buyer.objects.filter(username=username).first()
            if user :
                web_password = set_password(password)
                if user.password == web_password:
                    response = HttpResponseRedirect('/buyer/index/')
                    #登录校验
                    response.set_cookie('username',username)
                    request.session['username'] = username
                    # 方便其他查询
                    response.set_cookie('user_id',user.id)
                    return response
    return render(request,'buyerapp/login.html')

# 注册
def register(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')

        buyer = Buyer()
        buyer.username = username
        buyer.password = set_password(password)
        buyer.email = email
        buyer.save()
        return HttpResponseRedirect('/buyer/login/')
    return render(request,'buyerapp/register.html')

# 退出
def logout(request):
    response = HttpResponseRedirect('/buyer/login/')
    for key in request.COOKIES:
        response.delete_cookie(key)
    del request.session['username']
    return response

# 首页
@ loginValid
def index(request):
    result_list =[] #定义一个容器用来存放结果
    goodstype_list = GoodsType.objects.all() #查询所有类型
    for goods_type in goodstype_list: #循环类型
        goods_list = goods_type.goods_set.values()[:4] #查询前四条
        if goods_list: # 如果类型对应的值存在
            goodsType = {
                'id':goods_type.id,
                'name':goods_type.name,
                'description':goods_type.description,
                'picture':goods_type.picture,
                'goods_list':goods_list
            }# 构造输出结果
            # 查询类型当中有数据的数据
            result_list.append(goodsType) # 将数据存放到列表容器

    return render(request, 'buyerapp/index.html',locals())

# 商品列表
@ loginValid
def goods_list(request):
    goodslist = []
    type_id = request.GET.get('type_id')
    # 获取类型
    goods_type = GoodsType.objects.filter(id = type_id).first()
    if goods_type:
        # 查询所有的上架商品
        goodslist = goods_type.goods_set.filter(goods_state = 1)
    return render(request,'buyerapp/goods_list.html',locals())

# 商品支付结果
@ loginValid
def pay_result(request):
    '''
    支付宝支付成功自动用get请求返回的参数
    #编码
    charset=utf-8
    #订单号
    out_trade_no=10002
    #订单类型
    method=alipay.trade.page.pay.return
    #订单金额
    total_amount=1000.00
    #校验值
    sign=enBOqQsaL641Ssf%2FcIpVMycJTiDaKdE8bx8tH6shBDagaNxNfKvv5iD737ElbRICu1Ox9OuwjR5J92k0x8Xr3mSFYVJG1DiQk3DBOlzIbRG1jpVbAEavrgePBJ2UfQuIlyvAY1fu%2FmdKnCaPtqJLsCFQOWGbPcPRuez4FW0lavIN3UEoNGhL%2BHsBGH5mGFBY7DYllS2kOO5FQvE3XjkD26z1pzWoeZIbz6ZgLtyjz3HRszo%2BQFQmHMX%2BM4EWmyfQD1ZFtZVdDEXhT%2Fy63OZN0%2FoZtYHIpSUF2W0FUi7qDrzfM3y%2B%2BpunFIlNvl49eVjwsiqKF51GJBhMWVXPymjM%2Fg%3D%3D&trade_no=2019072622001422161000050134&auth_app_id=2016093000628355&version=1.0&app_id=2016093000628355
    #订单号
    trade_no=2019072622001422161000050134
    #用户的应用id
    auth_app_id=2016093000628355
    #版本
    version=1.0
    #商家的应用id
    app_id=2016093000628355
    #加密方式
    sign_type=RSA2
    #商家id
    seller_id=2088102177891440
    #时间
    timestamp=2019-07-2
    '''

    return render(request,'buyerapp/pay_result.html')

# 商品支付
@ loginValid
def pay_order(request):
    money = request.GET.get('money')
    order_id = request.GET.get("order_id")


    # 公钥
    alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsT2a5eY/3xnxh8AlC7jxcgE/FUHPfw6gnzohK000LPzp3slpdvDLrl+EJnG5SuZbsM3BYg41K8F5kCdthxQiJGvg++a+UAcQdGzw190eVjogtHOtXZcCseLV66B47oBfYCSOb3gLn31EB7h5zUG2DQEtpMKmjbIgQTJfv+CKxjyaiTXXpKgpb06/WTsMPIuwXOlWG1Uei3mOJt6ZnF914q/kNJWIjiEq/ubMsRTrWpK4OoQ636ZlEsJTUxSJm06mBE5uXBCDJSd952/b7NEEtyOYz7UpW9RZC5BDGK3M+/pmPsoBMUDK8Mh6KVnY3a13u2/f9q8MsQcydfJAcpr/UwIDAQAB
    -----END PUBLIC KEY-----"""

    # 私钥
    app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
    MIIEowIBAAKCAQEAsT2a5eY/3xnxh8AlC7jxcgE/FUHPfw6gnzohK000LPzp3slpdvDLrl+EJnG5SuZbsM3BYg41K8F5kCdthxQiJGvg++a+UAcQdGzw190eVjogtHOtXZcCseLV66B47oBfYCSOb3gLn31EB7h5zUG2DQEtpMKmjbIgQTJfv+CKxjyaiTXXpKgpb06/WTsMPIuwXOlWG1Uei3mOJt6ZnF914q/kNJWIjiEq/ubMsRTrWpK4OoQ636ZlEsJTUxSJm06mBE5uXBCDJSd952/b7NEEtyOYz7UpW9RZC5BDGK3M+/pmPsoBMUDK8Mh6KVnY3a13u2/f9q8MsQcydfJAcpr/UwIDAQABAoIBAEsQeEXd2jc22aBQtF/emANcm8b49FQvcb998wZP0EUtaC8+xjfli53yPhm6GGusXDDpM3m/4q0BZ+axjCWlVUBvn/2PoBJsq39jlC0YLPz/6VIDm+0DQ9Tq6Qa+E/mOzNX/JYP4J5QIjYNnkc5ogh3H3fjlp3xjcF2sY/jztFJ4Kv49B7i18AkXDXf2mwFyzOOvppBMT4WNj+ZXYZEhIykXOfA2FFXJ6sgayyhxfAYKt5uVkcTvETo9UWadfGQyjGrti+35VCjpFjhiaMbmRVFFI3dTtnntFf8078OrTP5Tjd4qq5KEgs7l1GwKZlqhrifLrdGG3+SDQnxDVelrVOECgYEA6vm/QRu2j8GAyME80BSmuF/37kAHJUxqHlJo6nZnLNHVKoETIM00RsbLOYfEFDrz6wcvljKjR8uHZU1Zi9SDjsC5SRvf0ZWjw5fQh83ThNZxm3ZHSR9e9iznM22qh02usxC28V5ITbnHQxHeKwIuUctznKidO+3qw6otfPP3LD8CgYEAwRln2YQ0xoNGgXe/fVha5NFUoHzefCAPbGZXSQYkqjijzQBbcPpiPhvL2yWCh+HDMx1LcccDkvRh0XfG19XIGMzE7rDGm1SVxsRraNfCP1sxq1UCdsf0aMUaesM5ITczRmddPMkellgqZNvNHdrVEIajoZeXPnzDmpefQqhat+0CgYBPpym2IHbadHX7l8XNo7KAfcfF8954PlcawETgdhKzls30Ap1BWU6HT4xEjEljsjhNS7pN6AyBofTb2kSoqfmOwrYMmm5c1aUWALin0JYLScZpNMcleoTuXnphbKOKCkNWYCwj1hocfwWVLtFpMuwQvi8Kw/3I+vXCLkYNPYZkcQKBgQCRbd7m1UkiERByxYs0jey21GkWDbVKaqLzEwi9+KB4ivvik1hK+GgxOqIHxHJQgFmRD4kYgbhRXzikl77sIxf2hZHz6rNJnSTIdHoolga3zKjVzspyRxnuJjRRLOLD/1zgs0xnUVl2BaS4HUqYJ428SorGUvMXnsN6lKLfgwf/6QKBgGapswT/Ml/4pPwjyA3ECoCji1b6uxTV+X6kZXKxv4CuRFOQzGCqRHCi1W1Lv3plnnQ1g53lzTmW4MQOFTvl/Y8yX+fHokhH/1PrAZcuKLwUa3HgDr9fEabmebtQf4hDtPQO4+tf4U/Ou9vdTTtcJ19BQuWmg0PzrwpO5agCYyqS
    -----END RSA PRIVATE KEY-----"""

    # 实例化支付请求
    alipay = AliPay(
        appid="2016101000652534",
        app_notify_url=None,
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2"
    )

    # 发起支付请求
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_id,  # 订单号
        total_amount=str(money),  # 支付金额
        subject='生鲜交易',  # 交易主题
        return_url="http://127.0.0.1:8000/buyer/pr/",
        notify_url="http://127.0.0.1:8000/buyer/pr/"
    )
    order = Order.objects.get(order_id = order_id)
    order.order_status = 2
    order.save()

    return HttpResponseRedirect("https://openapi.alipaydev.com/gateway.do?" + order_string)


# 用户中心
@ loginValid
def user_center(request):

    #buyer = Buyer.objects.filter(id = user).first()

    return render(request,'buyerapp/user_center.html',locals())

# 购物车
@ loginValid
def shopping_cart(request):

    return render(request,'buyerapp/shopping_cart.html')


# 全部订单
@ loginValid
def order_list(request):

    return render(request,'buyerapp/order_list.html')

# 设置订单编号
# 时间+用户id+商品id+店铺id

def setOrderId(user_id,goods_id,store_id):
    strtime = time.strftime('%Y%m%d%H%M%S',time.localtime())
    return strtime+user_id+goods_id+store_id

# 提交订单
@ loginValid
def submit_order(request):
    if request.method == "POST":
        # post 数据
        count = int(request.POST.get('count'))
        goods_id = request.POST.get('goods_id')
        #cookie 的数据
        user_id = request.COOKIES.get('user_id')
        print(user_id)
        #数据库的数据
        goods = Goods.objects.get(id=goods_id)
        store_id = goods.store_id.id #获取商品对应的店铺id
        price = goods.goods_price

        order = Order()
        order.order_id = setOrderId(str(user_id),str(goods_id),str(store_id))
        order.order_count = count
        order.order_user = Buyer.objects.get(id = user_id)
        order.order_price = count*price
        order.save()

        order_detail = OrderDetail()
        order_detail.order_id = order
        order_detail.goods_id = goods_id
        order_detail.goods_name = goods.goods_name
        order_detail.goods_price = goods.goods_price
        order_detail.goods_number = count
        order_detail.goods_total= count*goods.goods_price
        order_detail.goods_store = store_id
        order.order_status = 1
        order_detail.save()

        detail = [order_detail] # order_detail 作为类模型不可以迭代，所以转化为列表类型

        return render(request,'buyerapp/submit_order.html',locals())
    else:
        return HttpResponse('非法请求！')


# 商品详情
@ loginValid
def goods_description(request):
    goods_id = request.GET.get('goods_id')
    if goods_id:
        goods = Goods.objects.filter(id = goods_id).first()
        if goods:
            return render(request,'buyerapp/goods_description.html',locals())
    return HttpResponse('商品不存在')


# 收货地址
@ loginValid
def receive_adress(request):
    if request.method == 'POST':
        recver = request.POST.get('recver')
        address = request.POST.get('address')
        recv_phone = request.POST.get('recv_phone')
        post_number = request.POST.get('post_number')
        buyer_id = request.COOKIES.get('buyer_id')

        re_address = Address()
        re_address.recver = recver
        re_address.address = address
        re_address.recv_phone = recv_phone
        re_address.post_number = post_number
        re_address.buyer_id = Buyer.objects.get(id = buyer_id)
        re_address.save()


    return render(request,'buyerapp/receive_adress.html')



