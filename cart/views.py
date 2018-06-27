from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from products.models import Product

# Create your views here - CART.
def view_cart(request):
    cart = request.session.get('cart', {})
    totals = 0
    products = []
    
    for p in cart:
        print(p)
        product = get_object_or_404(Product, pk=p)
        print(product)
        products.append({
            'product' : product,
            'quantity': cart[p],
            'price': product.price,
            'image': product.image,
            'total': (cart[p] * product.price)
        })
        totals += cart[p] * product.price

    
    return render(request, 'cart/cart.html', {'cart': products, 'totals': totals})

def remove_item(request): 
    
    id = request.POST['product_id']
    products = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')


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
    return HttpResponse(cart[id])