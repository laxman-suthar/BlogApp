from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    blog_title=models.CharField(max_length=30)
    blog_text=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)
  
