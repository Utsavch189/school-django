from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from sc.models import class5, notic,Contact,class10,class9,class8,class7,class6
from django.contrib import messages
from datetime import datetime


def home(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        messages.success(request,'submitted suucessfully')
        contact.save()
    return render(request,'home.html')




def notice(request):
    noti=notic.objects.all()
    
    return render(request,'notice.html',{'noti': noti})


def contact(request):
    return render(request, 'contact.html')



def clas(request):
    c5=class5.objects.all()
    c6=class6.objects.all()
    c7=class7.objects.all()
    c8=class8.objects.all()
    c9=class9.objects.all()
    c10=class10.objects.all()
   
    if User.is_anonymous:
        return redirect('/login')
   
  
    return render(request,'clas.html',{'c5':c5},{'c6':c6},{'c7':c7},{'c8':c8},{'c9':c9},{'c10':c10})

def clas5(request):
    c5=class5.objects.all()
    return render(request,'clas5.html',{'c5':c5})

def clas6(request):
    c6=class6.objects.all()
    return render(request,'clas6.html',{'c6':c6})

def clas7(request):
    c7=class7.objects.all()
    return render(request,'clas7.html',{'c7':c7})

def clas8(request):
    c8=class8.objects.all()
    return render(request,'clas8.html',{'c8':c8})

def clas9(request):
    c9=class9.objects.all()
    return render(request,'clas9.html',{'c9':c9})

def clas10(request):
    c10=class10.objects.all()
    return render(request,'clas10.html',{'c10':c10})




def login_user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'clas.html')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return render(request,'login.html')
