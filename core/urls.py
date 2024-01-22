from django.urls import path
from . import views
urlpatterns=[
    path('', views.landing, name="landing"),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout')
]