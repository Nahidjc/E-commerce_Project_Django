from django.shortcuts import render
#import views
from django.views.generic import ListView, DeleteView

# Models
from App_Shop.models import Product
# Create your views here.


class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'
