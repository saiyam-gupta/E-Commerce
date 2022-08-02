import imp
from operator import index
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Store.models.product import Product
from Store.models.category import Category
from django.views import View

# Create your views here.
class Index(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = Product.get_all_products()
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_Categoryid(categoryID)
        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request,'index.html',data)

    def post(self,request):
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1 :
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1 
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('homepage')
        


   



    




    
    


    