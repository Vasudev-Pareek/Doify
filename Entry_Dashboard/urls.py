from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', Entery_Welcome_Dashboard_View, name="Entery_Welcome_Dashboard_View"),
    path('User_Registration', Registration_View, name="User_Registration"),
    path('User_Login', Login_View, name="User_Login"),
]
