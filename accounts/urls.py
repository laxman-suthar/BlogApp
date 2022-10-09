from django.urls import path

from .views import  Profie_edit, Register, login, logout_view, pass_word

urlpatterns=[
    path("register/",Register.as_view(),name="register"),
    path("logout/",logout_view,name="logout"),
    path("login/",login.as_view(),name="login"),
    path("profile/<int:pk>",Profie_edit.as_view(),name="profile"),
    path("password/",pass_word.as_view(),name="password")
]   