from django.urls import path

from .views import *

urlpatterns=[
    path("register/",register,name="register_page"),
    path("login/",login_page,name="login_page"),
    path("index/",index_page,name="indexpage"),
]