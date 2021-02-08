from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=50,default="")
    Email=models.CharField(max_length=50,default="")
    Phone=models.CharField(max_length=50,default="")
    Message=models.TextField(default="")
    def __str__(self):
        return self.Email
class Submit(models.Model):
    Sub_mail=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.Sub_mail
class recipt(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="static/rcp/")
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class blogPost(models.Model):
    title=models.CharField(max_length=50)
    post=models.TextField()
    image=models.ImageField(upload_to="static/blogimage")
    date=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.title
    