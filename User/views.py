from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import user_normal
from .forms import userREF
from django.contrib.messages.storage import session

# Create your views here.
def login(request):
    return render(request,'login.html')

def logcode(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd=request.POST['pwd']
        obje=user_normal.objects.get(email=email)
        if obje.password==pwd:
            request.session['email']=email
            request.session['username']=obje.username
            return render(request,'home.html',{"username" : obje.username, "email":obje.email})
        else:
            return HttpResponse('<h1>Invalid Password</h1>')

def Is_logged_in(request):
    return render(request,'home.html')
    
def registration(request):
    return render(request,'registration.html')
    
def register_view(request):
    return render(request,'register_user.html')

def register_user(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['password']
        obj=user_normal()
        obj.username=username
        obj.email=email
        obj.password=pwd
        obj.save()
        return render(request,'login.html')