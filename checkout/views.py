from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm
from products.models import Product
from .models import OrderLineItem
from django.conf import settings

# Create your views here.
def checkout(request):
    order_form = OrderForm()
    payment_form = MakePaymentForm()
    
    return render(request, "checkout/checkout.html", {'order_form': order_form, 'payment_form': payment_form})