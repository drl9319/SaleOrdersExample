from django.contrib import admin

from .models import Client, Product, SaleOrder, SaleOrderLine

admin.site.register(Client)

admin.site.register(Product)

admin.site.register(SaleOrder)

admin.site.register(SaleOrderLine)
