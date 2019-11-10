from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portal-home'),
    path('register', views.register, name='portal-register'),
]