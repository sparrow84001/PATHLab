from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import emp,user_normal
from .forms import userREF

# Create your views here.
def login(request):
    return render(request,'login.html')

def logcode(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd=request.POST['pwd']
        #print(email,pwd) # test perpuse
        obj=emp()
        obj.exampleInputEmail1=email
        obj.exampleInputPassword1=pwd
        obj.save()
        return render(request,'login.html')

def Is_logged_in(request):
    return render(request,'home.html')
    
def registration(request):
    return render(request,'registration.html')
    
def register_view(request):
    return render(request,'register_user.html')

def register_user(request):
    if request.method=='POST':
        #print('super')
        username=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['password']
        obj=user_normal()
        obj.username=username
        obj.email=email
        obj.password=pwd
        obj.save()
        return render(request,'login.html')