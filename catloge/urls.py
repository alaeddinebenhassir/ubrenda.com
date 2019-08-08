from django.urls import path, include 
from . import views

urlpatterns = [
    path('' , views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('categorie/' , views.show_categories , name= 'show_categories'),
    #path('categorie/<slug:slug>', views.show_categorie, name = 'show_categorie'),
    path('itm/?P<slug:slug>$' , views.show_product , name= 'show_product'),
    path('itm/shop/?P<slug:slug>' , views.by_product , name = 'by_product'),
    path('itm/shop/checkout/' , views.checkout , name = 'checkout'),
    path('itm/shop/Order/' , views.makeOrder , name = 'makeOrder'),
    path('paypal/',views.paypalCeckout , name = 'paypalcheckout')
    
]
