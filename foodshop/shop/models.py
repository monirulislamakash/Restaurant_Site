from django.db import models

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
    