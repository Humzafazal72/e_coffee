from django.urls import path
from . import views

urlpatterns = [
   path("",views.index,name="index"),
   path("about/",views.about,name="about"),
   path("shop/",views.shop,name="shop"),
   path("contact/",views.contact,name="contact"),
   path("cart/",views.cart,name="cart"),
   path("add_to_cart/<str:name>",views.add_to_cart,name="add_to_cart")
]