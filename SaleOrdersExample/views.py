from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
import json

from .models import Product



def index(request):
    GetProducts = requests.get('http://127.0.0.1:8000/Product/')
    ProductsData = GetProducts.json()
    ProductList = {'products':{'Product' + str(i) : j for i,j in enumerate(ProductsData)}}
    return render(request, 'SaleOrdersExample/index.html', ProductList)
