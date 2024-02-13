from django.shortcuts import render, redirect
from .models import customer
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from . import data


# Create your views here.
def landing(request):
    return render(request, 'landing.html')
def home(request):
    return render(request, 'home.html', {'y': data.data})
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def signin(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        authentication=authenticate(username=username, password=password)
        if authentication is not None:
            login(request, authentication)
            return render(request, 'home.html')
        else:
            return render(request, 'registration/signin.html')
    return render(request, 'registration/signin.html')
def signup(request):
    if request.method=='POST':
        try:
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']

            authenticationUserName=customer.objects.filter(username=username).first()
            authenticationEmail=customer.objects.filter(email=email).first()
            if not(authenticationEmail and authenticationUserName):
                newUser=User.objects.create_user(username, email, password)
                newCustomer=customer(firstname=firstname, lastname=lastname, email=email, username=username, password=password)
                newUser.first_name=firstname
                newUser.last_name=lastname

                newUser.save()
                newCustomer.save()
            else:
                return redirect('signup')

        except IntegrityError as e:
            return render(request, 'registration/signup.html')
        return redirect('signin')

    return render(request, 'registration/signup.html')
def signout(request):
    logout(request)
    return redirect('home')
def watchlist(request):
    return render(request, 'watchlist.html')