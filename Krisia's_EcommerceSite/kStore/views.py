from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from . models import productTable, cartCounter
from django.contrib import messages
from django.urls import reverse
from django.forms import ModelForm

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    products = productTable.objects.all()
    cartCount = cartCounter.objects.get(id=1)
    context  = {
        'myList':products,
        'cart': cartCount.count
    }  
    return HttpResponse(template.render(context))


def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())

def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())

def details(request):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render())

def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def addToCart(request):
    myCart = cartCounter.objects.get(id=1)
    myCart.count = myCart.count + 1
    myCart.save()
    messages.success(request, 'Added To Cart Successfully')
    return HttpResponseRedirect(reverse('index'))
    