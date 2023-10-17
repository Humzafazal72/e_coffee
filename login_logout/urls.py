from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_,name="login"),
    path('register/',views.register,name="register"),
    path("login_form/",views.login_form,name="login_form"),
    path('logout/',views.logout_,name="logout")
]