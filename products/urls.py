from django.urls import path
from .views import get_products, add_to_cart

urlpatterns = [
    path('products/', get_products, name='products'),
    path('<int:id>/added', add_to_cart, name='cart')
    ]