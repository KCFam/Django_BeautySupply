from django.db import models
from Order import Order
from Product import Product
from Delivery import Delivery


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField()
    discount = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    note = models.TextField(blank=True)

    def __str__(self):
        return '{} - {}:{}-{}'.format(self.order, self.product, self.sale_price, self.quantity)
