from django.shortcuts import render,redirect
from .models import Contact,Submit,recipt
from .models import blogPost
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
    blogpost=blogPost.objects.order_by("-date")
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
#Rejister
def singup(request):
    email=request.POST.get("email")
    passw=request.POST.get("password")
    cpassw=request.POST.get("confirmpassword")
    if request.method == "POST":
        if passw==cpassw:
            try:
                user=User.objects.get(username=email)
                return render(request,"singup.html",{'error':"User Alrady Exist"})
            except User.DoesNotExist:
                user=User.objects.create_user(username=email,password=passw)
                return render(request,"singup.html",{'error':"User Create Sucessfully"})
        else:
            return render(request,"singup.html",{'error':"Password Not Match"})
    return render(request,"singup.html")
#login
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passw=request.POST.get('password')
        user=auth.authenticate(username=email,password=passw)
        if user is not None:
            auth.login(request,user)
            return redirect(blogpost)
    return render(request,"login.html")
#BlogPost
def blogpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            title=request.POST.get('title')
            post=request.POST.get('post')
            pic=request.FILES['bpimg']
            blogpost=blogPost(title=title,post=post,image=pic)
            blogpost.save()
            return render(request,'blogpost.html')
        return render(request,'blogpost.html')
    else:
        return render(request,'login.html')
#Log Out 
def logout(request):
    auth.logout(request)
    return redirect(login)