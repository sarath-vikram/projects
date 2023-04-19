from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=200)   
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name    
    
class Supplier(models.Model):
    name = models.CharField(max_length=200) 
    mobile_sup = models.CharField(max_length=100)  
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=200) 
    mobile_cus = models.CharField(max_length=100)  
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.customer_name    
    
class Product(models.Model):

    
    unique_id = models.CharField(unique=True,max_length=150,null=False)
    name = models.CharField(max_length=255) 
    receive_quantity = models.PositiveIntegerField(default=0,blank=True,null=True)
    issue_quantity = models.PositiveIntegerField(default=0,blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand,on_delete=models.CASCADE) 
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    reorder_level = models.PositiveIntegerField(default=0,blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + str (self.receive_quantity)  