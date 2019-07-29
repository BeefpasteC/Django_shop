from alipay import AliPay

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
    appid = "2016101000652534",
    app_notify_url = None,
    app_private_key_string = app_private_key_string,
    alipay_public_key_string = alipay_public_key_string,
    sign_type = "RSA2"
)

# 发起支付请求
order_string = alipay.api_alipay_trade_page_pay(
    out_trade_no = '10001', #订单号
    total_amount= str(10000), #支付金额
    subject = '生鲜交易', # 交易主题
    return_url= None,
    notify_url=None
)
print("https://openapi.alipaydev.com/gateway.do?"+order_string)






