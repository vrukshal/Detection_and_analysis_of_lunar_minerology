from django.db import models

# Create your models here.

class user_details(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=20,default='1234')
    gender = models.CharField(max_length=10,default='1',choices=(('1','Male'),('2','Female'),('3','Other')))