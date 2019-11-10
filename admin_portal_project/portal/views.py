from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'portal/home.html')

def register(request):
    return render(request, 'portal/register.html')