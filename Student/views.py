from django.shortcuts import render,HttpResponse

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
