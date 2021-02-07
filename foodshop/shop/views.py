from django.shortcuts import render,redirect
from .models import Contact,Submit
# Create your views here.
#HomePage
def index(request):
    return render(request,"index.html")
#AboutPage
def about(request):
    return render(request,"about.html")
#BlogPage
def blog(request):
    return render(request,"blog.html")
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
    return render(request,"recipe.html")
#Sub
def sub_mail(request):
    if request.method=="POST":
        Sub_mail=request.POST.get("sub_mali")
        Sub_mail=Submit(Sub_mail=Sub_mail)
        Sub_mail.save()
    return redirect(index)