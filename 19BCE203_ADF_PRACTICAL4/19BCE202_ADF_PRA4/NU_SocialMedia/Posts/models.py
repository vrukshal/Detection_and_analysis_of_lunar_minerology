from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post_details(models.Model):
    Post_owner=models.CharField(max_length=50,default='')
    Post_title=models.CharField(max_length=50)
    Post_Content=models.CharField(max_length=100)
    Post_Image=models.ImageField(default="D:/sem7/ADF/LAB/NU_SocialMedia/826405.fig.0010a.jpg")
    Post_comment=models.TextField(default='')
    Post_like=models.IntegerField(default=0)

class comment(models.Model):
    container=models.ForeignKey(post_details,on_delete=models.CASCADE, db_index=True)
    value=models.CharField(max_length=200, db_index=True)
    comment_owner=models.CharField(max_length=50,default='')