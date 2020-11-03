from django.db import models
from Supplier import Supplier
from Product import Product


class SupplierProduct(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    minimum_order = models.PositiveIntegerField()
    mininum_order_price = models.DecimalField(max_digits=7, decimal_places=2)
    retail_price = models.DecimalField(max_digits=7, decimal_places=2)
    note = models.TextField(blank=True)

    def __str__(self):
        return '{} - {}:{}'.format(self.supplier, self.product, self.retail_price)
