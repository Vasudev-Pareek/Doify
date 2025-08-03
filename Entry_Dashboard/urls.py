from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', Entery_Welcome_Dashboard_View, name="Entery_Welcome_Dashboard_View"),
]
