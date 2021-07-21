from django.shortcuts import render, redirect
from . import models
# Create your views here.

# 首页
def toFirstPage(request):
    return render(request, 'index.html')
# 注册页
def toLogIn(request):
    return render(request, 'LogIn.html')
# 登录
def LogIn(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空

            qs = models.User.objects.values()
            user = qs.filter(name=username)
            if user:
                if qs.filter(name=username, passWord=password):
                    str = "?" + "username=" +  username + "/"
                    return redirect('/FindHouse/AddHouse' + str)
                else:
                    message = "密码不正确！"
            else:
                message = "用户名不存在！"
        return render(request, 'LogIn.html', {"message": message})
    return render(request, 'LogIn.html')
# 登录页
def toSignUp(request):
    return render(request, 'SignUp.html')

# 注册
def SignUp(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        phonenumber = request.POST.get('phonenumber', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and phonenumber and password:  # 确保用户名和密码都不为空
            #username = username.strip()
            qs = models.User.objects.values()
            user = qs.filter(name=username)
            if user:
                message = "该用户名已经存在！"
            else:
                record = models.User.objects.create(name = username,
                                                 phoneNumber = phonenumber,
                                                 passWord= password)
                message = "注册成功！请点击登录！"
                return render(request, 'SignUp.html', {"message": message, 'success': 1})

        return render(request, 'SignUp.html', {"message": message})
    return render(request, 'SignUp.html')