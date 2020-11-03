from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=5)
    country = models.CharField(max_length=20, default='USA')
    note = models.TextField(blank=True)

    def __str__(self):
        return '{} ,{} , {} {}'.format(self.street, self.city, self.state, self.postal_code)
