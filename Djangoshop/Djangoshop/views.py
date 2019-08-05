from django.core.mail import send_mail

def sendmail(request,):
    send_mail('307','啦啦啦啦啦','1453187816@qq.com',
              ['1453187816@qq.com','757077675@qq.com','574939795@qq.com'],fail_silently=False)