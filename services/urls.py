from django.urls import path
from . import views

urlpatterns = [
    #paths services
    path('services/', views.services, name='services'),
]    