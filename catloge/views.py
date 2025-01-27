from django.shortcuts import render ,redirect, get_object_or_404 
from .models import Item  ,Categorie
from .forms import SignUpForm
from django.contrib.auth import login, authenticate , logout
from django.http import JsonResponse
import json ,  stripe 

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

STRIPE_PUBLISHABLE_KEY = 'pk_test_eJzUry98i0m3vipsD9oQr2sB0013oq5o3f'
def show_product(request , slug ):
    p = get_object_or_404(Item , slug=slug)
    
    key = STRIPE_PUBLISHABLE_KEY
    
    return render(request , 'product.html' ,locals())

def test_items(request):
    p = Item.objects.all()
    return render(request , 'items.html' , locals())

def checkout(request):
    if  request.method == "POST" and request.is_ajax():
        stripe.api_key = 'sk_test_hf6QxTQLy7t4aP0LR3igPw8d00ru0S6dxC'
        email = request.POST['email']
        ship_to = request.POST['ship_to']

        token = request.POST['Token']
        name = request.session['name']
        charge = stripe.Charge.create(
            amount = int(float(request.session['price'])*100+50),
            currency='usd',
            description='Paid ' + name ,
            source=token,
            metadata={'order_id': 6735},
            )
        
        return JsonResponse({"message" : "Done" , 'token' : token , "data" : float(request.session['price'])+0.5})
        
    else :
        return JsonResponse({"message" : "ERROR"})

def by_product(request):
    if request.method == "POST":
        
        price = request.POST['price']
        request.session['price']= price

    return render(request , 'by_product.html' , {"pub_key" : STRIPE_PUBLISHABLE_KEY ,"data" : float(request.session['price'])+0.5})
