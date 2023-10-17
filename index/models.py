
from django.db import models

# Create your models here.

class customers(models.Model):
    email=models.EmailField(primary_key=True)
    u_name=models.TextField()

    def __str__(self) -> str:
        return f"{self.email}: {self.u_name}"
    
class Coffee(models.Model):
    name = models.CharField(max_length=25,primary_key=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self) -> str:
        return f"{self.name}"
    
class Cart(models.Model):
    user = models.ForeignKey(customers,on_delete=models.CASCADE)  # Assuming you have user authentication
    items = models.ManyToManyField(Coffee, through='CartItem')
    def __str__(self) -> str:
        return f"{self.user}'s Cart'"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self) -> str:
        return f"{self.cart}:{self.coffee}"
    
class order(models.Model):
    id=models.BigIntegerField(primary_key=True)
    total=models.DecimalField(max_digits=6, decimal_places=2)    
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)