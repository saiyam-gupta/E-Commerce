from django.db import models
from .product import Product
from .customer import Customer
import datetime
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default='1')
    price = models.IntegerField()
    address = models.CharField(max_length=80,default='', blank=True)
    phone = models.CharField(max_length=11, default="",blank = True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):

        temp =  Order.objects.filter(customer=customer_id)
        return temp.order_by('-date')
