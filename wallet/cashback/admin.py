from django.contrib import admin

from .models import Customer, Type, Product
# Register your models here.
admin.site.register(Customer)
admin.site.register(Type)
admin.site.register(Product)