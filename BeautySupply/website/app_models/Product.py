from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=100, blank=True)
    store_code = models.CharField(max_length=100, blank=True)
    PRODUCT_CATEGORY_CHOICES = [
        ('NAIL', 'Nail'),
        ('FACIAL', 'Facial'),
        ('HAIR', 'Hair'),
        ('EYELASHES', 'Eyelashes')
    ]
    category = models.CharField(
        max_length=20, choices=PRODUCT_CATEGORY_CHOICES, default='NAIL')
    customer_rate = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.customer_rate)
