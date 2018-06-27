from django.shortcuts import render, get_object_or_404, HttpResponse
from products.models import Product

# Create your views here - CART.
def view_cart(request):
    cart = request.session.get('cart', {})
    # return { 'cart_items': cart_items, 'total': total }
    
    
    products = []
    for p in cart:
        phone = get_object_or_404(Product, pk=p)
        products.append({
            'product' : phone,
            'quantity': cart[p],
            'price': phone.price,
            'total': (cart[p] * phone.price)
        })
    
    return render(request, 'cart/cart.html', {'cart': products})

def add_to_cart(request):

    # Get the product we're adding
    id = int(request.POST['product_id'])
    products = get_object_or_404(Product, pk=id)

    # Get the current cart
    cart = request.session.get('cart', {})
    
    # Update the cart
    cart[id] = cart.get(id, 0) + 1
    
    # Save the Cart back to the session
    request.session['cart'] = cart
    
    # Redirect somewhere
    return HttpResponse(cart[id])
