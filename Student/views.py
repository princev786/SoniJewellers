from django.shortcuts import render,redirect
from  django.contrib.auth.models import User
from  django.contrib.auth import authenticate,login,logout
from .models import Contacts
# Create your views here.
def index(request):
    return render(request,'index.html',{'titleName':"home"})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        msg = request.POST.get("msg")
        c= Contacts(name=name,emailid=email,phone=phone,msg=msg)
        c.save()
    return render(request,'contact.html')

def product(request,name):
    print("hello ",name)
    return render(request,'product.html',{'name':name})

def signupView(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName');
        lastName = request.POST.get('lastName');
        email = request.POST.get('email');
        userName = request.POST.get('userName');
        password = request.POST.get('password');
    
        user = User.objects.create_user(userName,email,password)
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        return redirect('/login')
    return render(request,"signup.html")

def loginView(request):
    if request.method=="POST":
        userName = request.POST.get('userName');
        password = request.POST.get('password');
        user = authenticate(username=userName, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request,user)
            return redirect('/home')
        else:
        # No backend authenticated the credentials
            return render(request,"login.html",{'error':"Username or Password is incorrect"})
        
    return render(request,"login.html")

def logoutView(request):
    logout(request)
    return redirect('/home')

