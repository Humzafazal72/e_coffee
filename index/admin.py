from django.contrib import admin
from .models import customers,Cart,CartItem,Coffee,order
# Register your models here.
admin.site.register(customers)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Coffee)
admin.site.register(order)

