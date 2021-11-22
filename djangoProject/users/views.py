import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import *

# Create your views here.
from django.views import View
from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User, Vacc


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        # User.objects.create(password=password,username=username)
        # User(username=username,password=password).save()
        user = authenticate(username=username,password=password)
        if user is None:
            return HttpResponse('用户名密码错误')
        else:
            login(request, user)
            # 跳转到首页
            response = redirect('/index')
            # 设置cookie
            # 登录状态，会话结束后自动过期
            response.set_cookie('is_login', True)
            # 设置用户名有效期一个月
            username = json.dumps(user.username)
            response.set_cookie('username', username, max_age=30 * 24 * 3600)
            return response

class IndexView(LoginRequiredMixin,View):
    def get(self,request):

        c = request.GET.get('page')
        info = Vacc.objects.all()
        p = Paginator(info, 3)
        try:
            pp = p.page(c)
        except Exception as e:
            pp = p.page(1)
        return render(request, 'index.html', context={'info': pp})
        # info = Vacc.objects.all()
        # return render(request,'index.html',{'info':info})
    def post(self,request):
        name = request.POST.get('name')
        address = request.POST.get('address')
        tag = request.POST.get('tag')
        info = Vacc.objects.filter(name__icontains=name,address__icontains=address,tag__icontains=tag)
        return render(request,'indexing.html',{"info":info})


class AddView(View):
    def get(self,request):
        return render(request,'add.html')
    def post(self,request):
        name = request.POST.get('name')
        instructions = request.POST.get('instructions')
        address = request.POST.get('address')
        tag = request.POST.get('tag')
        mobile = request.POST.get('mobile')
        vacc = Vacc(name=name,instructions=instructions,address=address,tag=tag,mobile=mobile)
        vacc.save()
        return redirect('/index')

class UpdateView(View):
    def get(self,request):
        id = request.GET.get('id')
        li = Vacc.objects.get(id=id)
        return render(request,'update.html',{'li':li})
    def post(self,request):
        id = request.GET.get('id')
        name = request.POST.get('name')
        instructions = request.POST.get('instructions')
        address = request.POST.get('address')
        tag = request.POST.get('tag')
        mobile = request.POST.get('mobile')
        Vacc.objects.filter(id=id).update(name=name,instructions=instructions,address=address,tag=tag,mobile=mobile)
        return redirect('/index')

def delete(request):
    id = request.GET.get('id')
    Vacc.objects.filter(id=id).delete()
    return redirect('/index')


class LogoutView(View):

    def get(self,request):
        # 清理session
        logout(request)
        # 退出登录，重定向到登录页
        response = redirect('/index')
        # 退出登录时清除cookie中的登录状态
        response.delete_cookie('is_login')

        return response