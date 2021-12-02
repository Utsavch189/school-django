from django.contrib import admin
from django.urls import path,include
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from sc import views
urlpatterns = [
    path("",views.home,name="home"),
    
    path("notice",views.notice,name="notice"),
    path("clas",views.clas,name="clas"),
    path("contact",views.contact,name="contact"),
    path("login",views.login_user,name="login"),
    path("logoutuser",views.logoutuser,name="logoutuser"),
    path("clas5",views.clas5,name="clas5"),
    path("clas6",views.clas6,name="clas6"),
    path("clas7",views.clas7,name="clas7"),
    path("clas8",views.clas8,name="clas8"),
    path("clas9",views.clas9,name="clas9"),
    path("clas10",views.clas10,name="clas10"),
]
