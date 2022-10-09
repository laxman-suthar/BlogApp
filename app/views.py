
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,View ,DetailView,DeleteView
from django.urls import reverse_lazy
from app.forms import Blogform
from .models import Blog

from django.contrib.auth.decorators import login_required
class home(TemplateView):
    template_name="home.html"
    
@login_required
def Blogs(request):
    if request.method=="POST":
        title=request.POST["blog_title"]
        text=request.POST["blog_text"]
        user=request.user
        user=Blog.objects.create(user=user,blog_title=title,blog_text=text)
        user.save()
        return redirect("home")
    return render(request,"blog.html",{"form":Blogform})

def BlogList(request):
    user=request.user
    queryset=Blog.objects.all().filter(user=user)
    return render(request,"bloglist.html",{"blogs":queryset})
    

class detail(DetailView):
    model=Blog
    template_name="detail.html"

class deleteview(DeleteView):
    queryset=Blog.objects.all()
    template_name="blog_confirm_delete.html"
    success_url=reverse_lazy("list")
    
