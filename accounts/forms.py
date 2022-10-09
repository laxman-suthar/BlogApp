from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.forms import UserChangeForm,AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django import forms
class Changeform(UserChangeForm):
    class Meta:
      model=User
      fields=["username","email","first_name","last_name"]
      exclude=["password",]

      

