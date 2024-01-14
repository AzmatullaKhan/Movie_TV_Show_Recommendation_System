from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, 'landing.html')
def home(request):
    return render(request, 'home.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def signin(request):
    return render(request, 'registration/signin.html')
def signup(request):
    return render(request, 'registration/signup.html')