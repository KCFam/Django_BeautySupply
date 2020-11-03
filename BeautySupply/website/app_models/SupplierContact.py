from django.db import models
from Supplier import Supplier
from Address import Address


class SupplierContact(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, blank=True, null=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return '{} - {}'.format(self.contact_name, self.phone)
