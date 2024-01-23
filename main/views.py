from django.shortcuts import render
from . import views
from main.models import *
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    return render(request,'main/index.html',{'product':products})

