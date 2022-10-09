from django.urls import path
from .views import BlogList, Blogs, deleteview, detail, home

urlpatterns=[
    path("home/",home.as_view(),name="home"),
    path("blog/",Blogs,name="blog"),
    path("blogList/",BlogList,name="list"),
    path("detail/<int:pk>",detail.as_view(),name="detail"),
    path("delete/<int:pk>" ,deleteview.as_view(),name="delete")
]