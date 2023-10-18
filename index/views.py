import random
from decimal import Decimal
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Coffee,customers,Cart,CartItem,order,ContactMessage
from django.contrib import messages

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

def contact_form(request):
    if request.method=='POST':
        name = request.POST['Name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)
        
        messages.success(request,f"We'll get back to you asap.")
        return redirect('contact')

def cart(request):
    if request.user.is_authenticated:
        customer=customers.objects.get(pk=request.user.username)
        cart=Cart.objects.get(user=customer)
        Cartitems=CartItem.objects.filter(cart=cart)
        total_all=[]

        for i in Cartitems:
            if i.quantity==0:
                i.delete()
                continue
            else:
                total_all.append(i.quantity*i.coffee.price)

        sub_total=sum(total_all)
        sub_total=Decimal(sub_total)

        id=random.randint(1,100000000)
        Order=order.objects.create(id=id,cart=cart,total=total)

        shipping=Decimal(10)
        if sub_total==0:
            shipping=0
                
        total=sub_total+shipping

        return render(request, 'cart.html',{'cartitem':Cartitems,'sub':sub_total,
                                            'total':total,'order_id':Order.id,'shipping':shipping})
    
    return redirect('shop')


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
    

def remove_coffee(request,name):
    customer=customers.objects.get(pk=request.user.username)
    cart=Cart.objects.get(user=customer)
    cartitems=CartItem.objects.filter(cart=cart,coffee=name)
    for i in cartitems:
        i.quantity-=1
        i.save()

    return redirect('cart')

def checkout(request,order_id):
    return HttpResponse("Work going on.....")

def finalize(request,order_id):
    Order=order.objects.get(id=order_id)
    cart=Order.cart
    #apply logic for employee view.
    cartitems=CartItem.objects.filter(cart=cart).delete()
    messages.success(request,f"Your order has been placed successfully!!")

    return redirect('shop')
