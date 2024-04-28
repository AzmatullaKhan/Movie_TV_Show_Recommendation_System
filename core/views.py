from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import customer
from .models import watchList
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from . import data
# import json


# Create your views here.
def landing(request):
    return render(request, 'landing.html')
def home(request):
    if request.method=='POST':
        index=int(request.POST['data_index'])
        username=request.POST['data_username']
        if(index<=5):
            index=index-1
            d=data.data_line1
        elif(index>5 and index<=10):
            index=(index % 5)
            if (index==0):
                index=4
            else:
                index=index-1
            d=data.data_line2
        else:
            index=(index % 5)
            if (index==0):
                index=4
            else:
                index=index-1
            d=data.data_line3
        newWatchlist=watchList(name=d[index]['name'], movie_id=d[index]['id'], genre=d[index]['genre'], 
                               url=d[index]['url'], desc=d[index]['desc'], director=d[index]['director'], writers=d[index]['writers'],
                               streaming=d[index]['streaming'], username=username)
        newWatchlist.save()
        return render(request, 'home.html', {'first': data.data_line1, 'second':data.data_line2, 'third':data.data_line3})
    return render(request, 'home.html', {'first': data.data_line1, 'second':data.data_line2, 'third':data.data_line3})
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
            global global_user
            global_user=username
            login(request, authentication)
            return redirect('home')
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
    if request.method == 'POST':
        index=request.POST['data_index']
        watchlist_index=watchList.objects.filter(name=index)
        watchlist_index.delete()
        # return redirect('watchlist')
        # watchList.save()
    watchlist_data=watchList.objects.filter(username=global_user)
    # json_watchlist_data=json.loads(watchlist_data)
    return render(request, 'watchlist.html',{'first':watchlist_data, 'name':global_user})
def resetpassword(request):
    return render(request, 'registration/resetpassword.html')
