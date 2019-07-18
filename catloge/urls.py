from django.urls import path, include 
from . import views

urlpatterns = [
    path('' , views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('categorie/' , views.show_categories , name= 'show_categories'),
    path('categorie/<slug:slug>', views.show_categorie, name = 'show_categorie'),
    path('<slug:slug>$' , views.show_products , name= 'show_cat_products'),
    path('items',views.test_items , name='items'),
    path('items/catloge/<slug:slug>$' , views.by, name='by_now')
]
