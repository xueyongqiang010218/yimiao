"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from users import views

from users.views import *
from people_user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view()),
    path('index/', IndexView.as_view()),
    path('add/', AddView.as_view()),
    path('update/', UpdateView.as_view()),
    path('delete/',views.delete),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisteredVies.as_view()),
    path('', PeopleLoginView.as_view()),
    path('peopleindex/', PeopleIndexView.as_view()),
    path('peopleadd/', PeopleAdd.as_view()),
    # path('reservation/', ReservationView.as_view()),
]
