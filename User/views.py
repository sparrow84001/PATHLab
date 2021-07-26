from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import emp

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
    
