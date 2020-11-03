from django.contrib import admin

from website.app_models.Address import Address
from website.app_models.Customer import Customer

# Register your models here.
admin.site.register(Address)
admin.site.register(Customer)
