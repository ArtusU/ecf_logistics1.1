from django.contrib import admin
from .models import (
    Referrer, 
    Recipient, 
    Delivery_Address, 
    Product_Tag, 
    Product, Order
    )

admin.site.register(Referrer)
admin.site.register(Recipient)
admin.site.register(Delivery_Address)
admin.site.register(Product_Tag)
admin.site.register(Product)
admin.site.register(Order)