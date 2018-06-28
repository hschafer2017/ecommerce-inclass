from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from products.models import Product
from products.views import get_products
from .utils import get_cart_items_and_total

# Create your views here - CART.

# Shows cart and items in it. 
def view_cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart/cart.html', get_cart_items_and_total(cart))

# Removing only one item, changing the quantity from 2 to 1. 
def remove_item(request): 
    id = request.POST['product_id']
    products = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] -= 1
        if cart[id] == 0:
            del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')

# Adding items to the cart. 
def add_to_cart(request):

    # Get the product we're adding
    id = request.POST['product_id']
    products = get_object_or_404(Product, pk=id)

    # Get the current cart
    cart = request.session.get('cart', {})
    
    # Update the cart
    cart[id] = cart.get(id, 0) + 1
    
    # Save the Cart back to the session
    request.session['cart'] = cart
    
    # Redirect somewhere
    return redirect('view_cart')