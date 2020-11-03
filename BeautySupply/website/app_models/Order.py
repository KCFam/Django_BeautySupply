from django.db import models
from Customer import Customer
from Employee import Employee
from Product import Product
from datetime import datetime


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=datetime.now)
    discount = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    ORDER_STATUS_CHOICES = [
        ('NEW', 'New'),
        ('ON HOLD', 'On hold'),
        ('PENDING SUPPLIER', 'Pending Supplier'),
        ('PENDING CUSTOMER', 'Pending Customer'),
        ('CONFIRMED', 'Comfirmed'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
        ('DELETED', 'Deleted')
    ]
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS_CHOICES, default='NEW')
    note = models.TextField(blank=True)
    order_products = models.ManyToManyField(Product, through='OrderProduct')

    def __str__(self):
        return '{}:{} - {} - {}'.format(self.status, self.order_date, self.customer, self.total)
