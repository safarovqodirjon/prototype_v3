from django.urls import path
from . import views
from django.contrib import admin

app_name = 'first'

urlpatterns = [

    path('home/', views.index, name='home')
]
