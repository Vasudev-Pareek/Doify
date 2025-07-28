from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', Notes_Entry_Page, name="Notes_Entry_Page"),
]
