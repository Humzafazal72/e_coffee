
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Coffee,customers,Cart,CartItem

def index(request):
    if not request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return render(request,'index.html',{'remove_login':True})

def shop(request):
    if not request.user.is_authenticated:
        return render(request,'shop.html')
    else:
        return render(request,'shop.html',{'remove_login':True})

def about(request):
    if not request.user.is_authenticated:
        return render(request,'about.html',)
    else:
        return render(request,'about.html',{'remove_login':True})

def contact(request):
    if not request.user.is_authenticated:
        return render(request,'contact.html')
    else:
        return render(request,'contact.html',{'remove_login':True})

def cart(request):
    if request.user.is_authenticated:
        customer=customers.objects.get(pk=request.user.username)
        cart=Cart.objects.get(user=customer)
        Cartitems=CartItem.objects.filter(cart=cart)

        return render(request, 'cart.html',{'cartitem':Cartitems})


def add_to_cart(request,name):
    if request.user.is_authenticated:
        customer=customers.objects.get(pk=request.user.username)
        type=Coffee.objects.filter(name=name).first() 
        cart=Cart.objects.get(user=customer)
        quantity=1
     
        try:
            cart_item_prev = CartItem.objects.get(coffee=type, cart=cart)
            quantity += cart_item_prev.quantity
            cart_item_prev.delete()
            CartItem.objects.create(coffee=type,cart=cart,quantity=quantity)
        except CartItem.DoesNotExist:
            CartItem.objects.create(coffee=type,cart=cart,quantity=quantity)
                

        return redirect('shop')
    