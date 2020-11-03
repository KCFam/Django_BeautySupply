from django.db import models
from Product import Product


class ProductInStore(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField()
    in_store_location = models.CharField(max_length=100, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return '{} - {}:{}'.format(self.product, self.quantity_in_stock, self.sale_price)
