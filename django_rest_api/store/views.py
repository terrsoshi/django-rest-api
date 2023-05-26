from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import *

class IndexView(ListView):
    model = Product
    context_object_name = 'products'
    template_name ='store/product_list.html'

class ShowView(DetailView):
    template_name = 'store/product.html'
    context_object_name = 'product'
    model = Product

class CartView(TemplateView):
    template_name ='store/cart.html'
    extra_context = {
        'items': [],
        'subtotal': 1.0,
        'tax_rate': int(ShoppingCart.TAX_RATE * 100.0),
        'tax_total': 2.0,
        'total': 3.0,
    }