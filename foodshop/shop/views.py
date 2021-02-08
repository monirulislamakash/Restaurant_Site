from django.shortcuts import render,redirect
from .models import Contact,Submit,recipt,blogPost
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
#HomePage
def index(request):
    dish=recipt.objects.all()
    VAR={
        "rep":dish
    }
    return render(request,"index.html",VAR)
#AboutPage
def about(request):
    return render(request,"about.html")
#BlogPage
def blog(request):
    blogpost=blogPost.objects.all()
    sevar={
        "blog":blogpost
    }
    return render(request,"blog.html",sevar)
#ContactPage
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("Phone")
        sms=request.POST.get("message")
        cfm=Contact(Name=name,Email=email,Phone=phone,Message=sms)
        cfm.save()
        return redirect(index)
    return render(request,"contact.html")
#RecipPage
def recip(request):
    dish=recipt.objects.all()
    VAR={
        "rep":dish
    }
    return render(request,"recipe.html",VAR)
#Sub_Mail
def sub_mail(request):
    if request.method=="POST":
        Sub_mail=request.POST.get("sub_mali")
        Sub_mail=Submit(Sub_mail=Sub_mail)
        Sub_mail.save()
    return redirect(index)
#Order Pages
def order(request):
    
    return render(request,"order.html")
#login
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passw=request.POST.get('password')
        user=auth.authenticate(username=email,password=passw)
        if user is not None:
            auth.login(request,user)
            return render(request,"index.html")
    return render(request,"login.html")