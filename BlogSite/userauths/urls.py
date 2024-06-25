from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings

from django.views.static import serve
from .views import register_user,login_user,logout_user
app_name = "userauths"
urlpatterns = [

path("register/",register_user,name="register"),
path("login/",login_user,name="login"),
path("logout_user",logout_user,name="logout_user")

]