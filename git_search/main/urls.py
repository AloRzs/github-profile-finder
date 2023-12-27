from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index/',main_view,name='index'),
    path('lista/',list_view,name='lista'),
]