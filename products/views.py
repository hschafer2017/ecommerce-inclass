from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse

# Create your views here - PRODUCTS.

def get_products(request): 
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

def add_to_cart(request, id):
    if request.method == 'POST':
        products = get_object_or_404(Product, id=id)
        return HttpResponse("You've added " + products.name)