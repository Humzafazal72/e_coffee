from django.contrib.auth.models import User
from index.models import customers,Cart
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username, password)
        
        # Check if the username is unique
        if User.objects.filter(email=email).exists():
            # Handle the case where the username is not unique
            pass
        else:
            # Create a new user
            user = User.objects.create_user( username=email, password=password)
            user.save()
            # Create a new customer instance
            customer, created = customers.objects.get_or_create(email=email, u_name=username)

            # Create a Cart object associated with the customer
            Cart.objects.create(user=customer)

            # Log the user in after registration
            login(request, user)

            # Redirect to the 'index' page
            return redirect('index')

    return render(request, 'login_form.html')

def login_(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'home' with the URL to redirect to after login
        else:
            return render(request, 'login_form.html', {'fail':True})

    return render(request, 'login_form.html')

def login_form(request):
    return render(request,'login_form.html',{'fail':False})

def logout_(request):
    logout(request)
    return redirect('index')