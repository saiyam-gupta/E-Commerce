from django.contrib import admin

from Store.models.customer import Customer
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
# Register your models here. IMPORTANT

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
class CustomerCategory(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','password','phone']

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,CustomerCategory)
admin.site.register(Order)
