from django.urls import path
from . import views

urlpatterns = [
    #paths services
    path('', views.services, name='services'),
]    