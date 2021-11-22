import json

from django.contrib.auth import login
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.shortcuts import *

# Create your views here.
from django.views import View

from people_user.models import People, Rescenter
from users.models import Vacc


class RegisteredVies(View):
    def get(self,request):
        return render(request,'registered.html')
    def post(self,request):
        mobile = request.POST.get('mobile')
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordtwo = request.POST.get('passwordtwo')
        id_number = request.POST.get('id_number')
        address = request.POST.get('address')
        unit = request.POST.get('unit')
        People(mobile=mobile,password=password,id_number=id_number,address=address,unit=unit,username=username).save()
        return redirect('/')


class PeopleLoginView(View):
    def get(self, request):
        return render(request, 'people_login.html')
    def post(self,request):
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        # User.objects.create(password=password,username=username)
        # User(username=username,password=password).save()
        if People.objects.filter(mobile=mobile,password=password):

            for i in People.objects.filter(mobile=mobile,password=password):
                request.session['id'] = i.id
                request.session['name'] = i.username
                return redirect('/peopleindex')
            return redirect('/peopleindex')
        else:
            return HttpResponse('手机号密码错误')

class PeopleIndexView(View):
    def get(self,request):
        c = request.GET.get('page')
        info = Vacc.objects.all()
        p = Paginator(info, 3)
        try:
            pp = p.page(c)
        except Exception as e:
            pp = p.page(1)
        return render(request, 'people_index.html', context={'info': pp})
    def post(self,request):
        name = request.POST.get('name')
        address = request.POST.get('address')
        tag = request.POST.get('tag')
        info = Vacc.objects.filter(name__icontains=name,address__icontains=address,tag__icontains=tag)
        return render(request,'people_indexing.html',{"info":info})
class PeopleAdd(View):
    def get(self,request):
        id=request.GET.get('id')
        peo_id=request.GET.get('peo_id')
        People.objects.filter(id=peo_id).update(vacc_id_id=id)

        peo_vacc = People.objects.filter(id=peo_id,vacc_id_id=id)
        for i in peo_vacc:
            Rescenter.objects.create(peo_id_id=peo_id,vacc_id_id=id,username=i.username,id_number=i.id_number,mobile=i.mobile,address=i.address,name=i.vacc_id.name,vaccaddress=i.vacc_id.address,vaccmobile=i.vacc_id.mobile,data=i.vacc_id.data)
        peo_test = Rescenter.objects.filter(peo_id=peo_id)
        return render(request,'reservation.html',{'peo_test':peo_test})

# class ReservationView(View):
#     def get(self,request):
#         id = request.session.get('id')
#         peo_test = People.objects.filter(id=id)
#         # vacc = Vacc.objects.all()
#         return render(request,'reservation.html',{'peo_test':peo_test})