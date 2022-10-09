from urllib import request
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
# Create your views here.
from django.contrib.auth.forms import PasswordChangeForm
from .forms import Changeform,AuthenticationForm

from django.views.generic import CreateView,UpdateView,DetailView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from django.contrib.auth.views import PasswordChangeView
# class Login(LoginView):
#     authentication_form

class Register(CreateView):
   form_class=UserCreationForm
   template_name="register.html"
   
   success_url=reverse_lazy("login")

def logout_view(request):
    messages.success(request,"you are logged out")
    logout(request) 
    return redirect("/home/")

class login(LoginView):
    template_name="login.html"
    form_class=AuthenticationForm
    
class Profie_edit(UpdateView):
    model=User
    fields=["username","email","first_name","last_name"]
    queryset=User.objects.all()
    template_name="profile.html"
    success_url=reverse_lazy("home",)


    
class pass_word(PasswordChangeView):
    form_class=PasswordChangeForm
    template_name="password.html"
    success_url=reverse_lazy("home")
