from django.db import models
from Purchase import Purchase
from Product import Product
from Employee import Employee


class PurchaseProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    received_check_employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=7, decimal_places=2)
    standard_price = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True)
    purchase_quantity = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    PURCHASE_PRODUCT_DELIVERY_STATUS_CHOICES = [
        ('IN SUPLLIER LOCATION', 'In supplier location'),
        ('ORDER READY', 'Order ready'),
        ('IN TRANSIT', 'In transit'),
        ('OUT FOR DELIVERY', 'Out for delivery'),
        ('DELIVERED', 'Delivered')
    ]
    delivery_status = models.CharField(
        max_length=30, choices=PURCHASE_PRODUCT_DELIVERY_STATUS_CHOICES, default='IN SUPLLIER LOCATION')
    last_status_update_time = models.DateTimeField(auto_now=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return '{}-{}'.format(self.purchase, self.product)
