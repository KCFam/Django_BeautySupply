from django.db import models
from Address import Address


class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField
    end_date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.phone)
