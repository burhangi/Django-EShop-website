from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product

register = template.Library()

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0



class Cart(View):
    def get(self, request):
        try:
            cart = request.session['cart']
        except KeyError:
            cart = {}

        ids = list(cart.keys())
        products = Product.get_product_by_id(ids)
        return render(request, 'cart.html', {'products': products})
