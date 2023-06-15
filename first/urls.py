from django.urls import path
from . import views

app_name = 'first'

urlpatterns = [
    path('', views.index, name='home')
]
