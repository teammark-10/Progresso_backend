from django.db import models

class User(models.Model):
    number = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    dob = models.CharField(max_length=250)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)

# number,name,email,gender,dob,weight,height
    
class otp(models.Model):
    number = models.CharField(max_length=250)
    otp = models.CharField(max_length=250)
