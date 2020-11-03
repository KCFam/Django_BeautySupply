from django.db import models
from Employee import Employee
from datetime import datetime


class Delivery(models.Model):
    delivery_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    DELIVERY_STATUS_CHOICES = [
        ('IN STORE', 'In store'),
        ('ORDER READY', 'Order ready'),
        ('IN TRANSIT', 'In transit'),
        ('OUT FOR DELIVERY', 'Out for delivery'),
        ('DELIVERED', 'Delivered')
    ]
    status = models.CharField(
        max_length=20, choices=DELIVERY_STATUS_CHOICES, default='IN STORE')
    delivery_date = models.DateTimeField(default=datetime.now)
    note = models.TextField(blank=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.delivery_employee, self.status, self.delivery_date)
