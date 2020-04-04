from django.db import models

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class RootAdmin(models.Model):

    name=models.CharField(max_length=20)
    email=models.EmailField()
    pwd=models.CharField(max_length=20)

class State(models.Model):
    name=models.CharField(max_length=30)

class City(models.Model):
    name=models.CharField(max_length=30)

class Branch(models.Model):
    landline_no=models.CharField(max_length=8)
    mobile_no=models.CharField(max_length=10)
    branch_proprietor_name=models.CharField(max_length=30)
    branch_opening_date=models.DateField()
    branch_locality = models.CharField(max_length=100)  # locality???
    city=models.ForeignKey(City,default=None)
    state=models.ForeignKey(State,default=None)
    zipcode = models.CharField(max_length=8)

class BranchUser(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    pwd=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    city = models.ForeignKey(City, default=None)
    state = models.ForeignKey(State, default=None)
    zipcode = models.CharField(max_length=8)
    branch=models.ForeignKey(Branch,default=None)

class ProductCategory(models.Model):
    name=models.CharField(max_length=50)

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(max_length=4)
    productcategory=models.ForeignKey(ProductCategory,default=None)

class Payment(models.Model):
    mode=models.CharField(max_length=15)

class Customer(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile_no=models.CharField(max_length=10)
    DOB=models.DateField()

class CustomerReview(models.Model):
    review_desc=models.CharField(max_length=100)
    review_date=models.CharField()
    customer=models.ForeignKey(Customer,default=None)


class BranchEmployee(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    salary=models.IntegerField(max_length=10) #re-condsider the size of this field
    UIDAI=models.CharField(max_length=12)
    address=models.CharField(max_length=100)
    city = models.ForeignKey(City, default=None)
    state = models.ForeignKey(State, default=None)
    zipcode=models.CharField(max_length=8)


class Order(models.Model):
    date=models.DateField()
    #TODO properly frame the fields of this table for the address and payment fields
    date=models.DateField()
    address = models.CharField(max_length=100)
    city = models.ForeignKey(City, default=None)
    state = models.ForeignKey(State, default=None)
    state = models.ForeignKey(State, default=None)
    zipcode = models.CharField(max_length=8)
    total_amt=models.IntegerField(max_length=5)
    discount=models.IntegerField(max_length=2)#percentage
    tax=models.IntegerField(max_length=2)#percentage
    payment=models.ForeignKey(Payment,default=None)
    customer=models.ForeignKey(Customer,default=None)

#Mapping multiple products to one order ID
class ProductOrderMap(models.Model):
    qty=models.IntegerField(max_length=50)
    total_per_qty_price=models.IntegerField(max_length=5) # what does this field signify
    product=models.ForeignKey(Product,default=None)
    order=models.ForeignKey(Order,default=None)

