from django.shortcuts import render,HttpResponse
from utils.smtp import send_mail
# Create your views here.
from app01 import models

def register(request):
    if request.method=='POST':
        email_user = request.POST.get('username')  # 发送者账号 '1060407136@qq.com'
        email_pwd = request.POST.get('pwd') # 发送者密码 'ekrpleslkrbrbdge'
        print(email_user,email_pwd)
        maillist = '2634491903@qq.com'
        title = '测试邮件标题'
        content = '哈哈，这是我的第一个python程序发送的邮件测试内容 爱你呦！'
        send_mail(email_user, email_pwd, maillist, title, content)
        return HttpResponse('ok')
    return render(request, 'register.html', locals())


