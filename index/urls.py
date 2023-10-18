from django.urls import path
from . import views

urlpatterns = [
   path("",views.index,name="index"),
   path("about/",views.about,name="about"),
   path("shop/",views.shop,name="shop"),
   path("contact/",views.contact,name="contact"),
   path("contact_form/",views.contact_form,name="contact_form"),
   path("cart/",views.cart,name="cart"),
   path("add_to_cart/<str:name>",views.add_to_cart,name="add_to_cart"),
   path("remove_coffee/<str:name>",views.remove_coffee,name="remove_coffee"),
   path("checkout/<int:order_id>",views.checkout,name="checkout"),
   path("finalize/<int:order_id>",views.finalize,name="finalize"),
]