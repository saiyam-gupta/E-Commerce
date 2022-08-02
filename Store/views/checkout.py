import imp
from itertools import product
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from Store.models.customer import Customer
from Store.models.product import Product
from Store.models.orders import Order
from Store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class CheckOut(View):
    @method_decorator(auth_middleware)

    def post(self,request):
       address = request.POST.get("Address")
       phone = request.POST.get("Phone")
       customer = request.session.get("customer")
       cart = request.session.get('cart')
       products = Product.get_products_by_id(list(cart.keys()))
       print(address, phone, customer, cart, products)

       for product in products:
           order = Order(customer=Customer(id=customer),product=product,price=product.price,quantity=cart.get(str(product.id)),address=address,phone=phone)
           order.save()
           request.session['cart'] = {}
           return redirect('cart')

		    
       


    
       