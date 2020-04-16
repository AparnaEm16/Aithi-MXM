# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import RootAdmin, State, City, Branch, BranchUser, ProductCategory, Product, Payment, Customer, \
    CustomerReview, BranchEmployee, Order, ProductOrderMap

# Register your models here.

admin.site.register(RootAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Branch)
admin.site.register(BranchUser)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(Customer)
admin.site.register(CustomerReview)
admin.site.register(BranchEmployee)
admin.site.register(Order)
admin.site.register(ProductOrderMap)
