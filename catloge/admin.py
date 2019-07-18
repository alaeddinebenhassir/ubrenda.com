from django.contrib import admin
from .models import Item ,Order ,Categorie ,Client 


@admin.register(Item) 
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','descreption' ,'ctgr' ,'price' ,'pubdate')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('clt' ,'itm' ,'ship_to' ,'orderdate')

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name','description' ,'slug' ,'is_active' 
        ,'meta_keywords' ,'meta_description' ,'created_at' ,'updated')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name' ,'email')


