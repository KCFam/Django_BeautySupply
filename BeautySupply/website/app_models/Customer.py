from django.db import models
from .Address import Address
from datetime import datetime


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    name_prefix = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, blank=True, null=True)
    become_customer_date = models.DateTimeField(default=datetime.now)
    is_accept_newletters = models.BooleanField(default=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return '{}, {}'.format(self.first_name, self.last_name)
