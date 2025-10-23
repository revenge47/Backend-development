from django.db import models
from django.urls import reverse
# Create your models here.
class Customer(models.Model):
    Phone_number = models.IntegerField(primary_key=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    date_and_time_created = models.DateTimeField(auto_now=True)

class Category(models.Model):
    Category_name = models.CharField(max_length=248, primary_key=True)
    #add subcategory
class Product(models.Model):
    Product_id = models.IntegerField(primary_key=True)
    Product_name = models.CharField(max_length=100)
    Product_image = models.ImageField(null=True,blank=True)
    Price = models.IntegerField()
    discount_price = models.IntegerField(null=True)
    Quantity = models.IntegerField()
    description = models.TextField(null=True)
    category = models.OneToOneField(Category, null=True, on_delete=models.CASCADE)
    #product_details
    def get_absolute_url(self):
        return reverse('store:prod',kwargs={'pk':self.Product_id})

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    billing_address = models.CharField(max_length=248)
    Shipping_address = models.CharField(max_length=248)
    date_and_time_ordered = models.DateTimeField(auto_now=True)
    #add time of delivery
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product =models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
