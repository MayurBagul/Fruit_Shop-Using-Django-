from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# We are gonna map product to index


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('Welcome To New Products')


