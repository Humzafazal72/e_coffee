from django.contrib import admin
from .models import customers,Cart,CartItem,Coffee
# Register your models here.
admin.site.register(customers)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Coffee)

