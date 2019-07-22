from django.shortcuts import render ,redirect, get_object_or_404 #, render_to_request 
from .models import Item  ,Categorie
from .forms import SignUpForm
from django.contrib.auth import login, authenticate , logout
from django.http import JsonResponse
import json

import stripe 
# Create your views here.

def index(request):
    product = Item.objects.all()
    c= Categorie.objects.all()
    
    return render(request, 'index.html', { 'product':product ,'c' : c})
    

def show_categories(request):
    c = Categorie.objects.all()
    product = Item.objects.all()
    return render(request ,'categories.html' ,locals())


def show_categorie(request , slug):
    c = Categorie.objects.all()
    p = get_object_or_404(Categorie ,slug=slug)
    products = Item.objects.all().filter(ctgr=p.pk)
    
    return render(request ,'products.html' , locals() )

STRIPE_PUBLISHABLE_KEY = 'pk_test_7K5UP2JIlnyNlNf3gRXpDQPD00ggfIRiZi'
def show_products(request , slug ):
    c = Categorie.objects.all()

    p = get_object_or_404(Item , slug=slug)
    
    key = STRIPE_PUBLISHABLE_KEY
    
    return render(request , 'product.html' ,locals())

def test_items(request):
    p = Item.objects.all()
    return render(request , 'items.html' , locals())

