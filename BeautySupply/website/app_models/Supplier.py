from django.db import models
from Product import Product
from Address import Address
from datetime import datetime


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, blank=True, null=True)
    became_supplier_date = models.DateTimeField(default=datetime.now)
    note = models.TextField(blank=True)
    supplier_products = models.ManyToManyField(
        Product, through='SupplierProduct')

    def __str__(self):
        return '{} - {}'.format(self.name, self.phone)
