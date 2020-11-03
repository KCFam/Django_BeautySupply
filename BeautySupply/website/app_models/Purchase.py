from django.db import models
from Supplier import Supplier
from Employee import Employee
from Product import Product
from datetime import datetime


class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    purchase_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(default=datetime.now)
    estimate_delivered_date = models.DateTimeField(default=datetime.now)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    PURCHASE_STATUS_CHOICES = [
        ('NEW', 'New'),
        ('ON HOLD', 'On hold'),
        ('PENDING SUPPLIER', 'Pending Supplier'),
        ('PENDING PAYMENT', 'Pending Customer'),
        ('CONFIRMED', 'Comfirmed'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
        ('DELETED', 'Deleted')
    ]
    status = models.CharField(
        max_length=20, choices=PURCHASE_STATUS_CHOICES, default='NEW')
    note = models.TextField(blank=True)
    purchase_products = models.ManyToManyField(
        Product, through='PurchaseProduct')

    def __str__(self):
        return '{}:{}-{}:{}'.format(self.supplier, self.purchase_date, self.total, self.status)
