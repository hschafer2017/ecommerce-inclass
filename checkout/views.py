from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm
from products.models import Product
from decimal import Decimal
from cart.utils import get_cart_items_and_total
from django.utils import timezone
from .models import OrderLineItem
from django.contrib import messages
import stripe
from django.conf import settings

# Create your views here - Checkout.

def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)    
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid():
            # Save The Order
            order = order_form.save()
           
        
            # Save the Order Line Items
            cart = request.session.get('cart', {})
            for product_id, quantity in cart.items(): 
                line_item = OrderLineItem()
                
                line_item.order = order
                line_item.products = get_object_or_404(Product, pk=product_id)
                
                line_item.quantity = quantity
                line_item.save()
        
            # Clear the Cart
            del request.session['cart']
            return HttpResponse("Checkout completed")
    else:
        cart = request.session.get('cart', {})
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        context = get_cart_items_and_total(cart)
        forms = {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE}
        context.update(forms)
    
    return render(request, "checkout/checkout.html", context)