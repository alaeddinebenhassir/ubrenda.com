from django.db import models
from django.db.models.signals import pre_save 
from django.utils.text import slugify 
from django.urls import reverse


class Categorie(models.Model):
  
    name= models.CharField(max_length=50 )
    description = models.TextField()
    slug = models.SlugField(max_length= 50 , blank=True,
        help_text = ' unique value for product url created frome name ')
    is_active = models.BooleanField(default = True)
    meta_keywords = models.CharField("Meta Keywords",max_length = 255 , help_text = 'for meta tags ')
    meta_description =  models.CharField("Meta Description ",max_length = 255 , help_text = 'for meta tags ')
    created_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return reverse('show_categorie', args=[self.slug])
    
    def __str__(self):
        return self.name

class sub_cotegorie(models.Model):
    parent = models.ForeignKey(Categorie, on_delete = models.CASCADE)
    name = models.CharField(max_length=50 )
    description = models.TextField()
    slug = models.SlugField(max_length= 50 , blank=True,
        help_text = ' unique value for product url created frome name ')
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    meta_keywords = models.CharField("Meta Keywords",max_length = 255 , help_text = 'for meta tags ')
    meta_description =  models.CharField("Meta Description ",max_length = 255 , help_text = 'for meta tags ')
    
    def get_absolute_url(self):
        return reverse('show_categorie', args=[self.slug])
    
    def __str__(self):
        return self.name
class Item(models.Model):
    name= models.CharField(max_length = 50 )  
    slug = models.SlugField(max_length = 255 , blank=True, unique= True , help_text = 'Unique product page url , created from Name ')   
    ctgr = models.ForeignKey(Categorie , on_delete = models.CASCADE)# ctgr = models.ManyToManyField(Categorie) 
    descreption = models.TextField(blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2 , null=True)
    old_price=models.DecimalField(max_digits = 8 , decimal_places = 2 , null=True)
    pubdate = models.DateTimeField(auto_now = True )
    img = models.ImageField(upload_to = 'img/product/', default = 'pic_folder/None/no-img.jpg')
    sub_img_1 = models.ImageField(upload_to = 'img/product/', default = 'pic_folder/None/no-img.jpg')
    sub_img_2 = models.ImageField(upload_to = 'img/product/', default = 'pic_folder/None/no-img.jpg')
    sub_img_3 = models.ImageField(upload_to = 'img/product/', default = 'pic_folder/None/no-img.jpg')
    brand = models.CharField(max_length = 255 , null=True)
    meta_description = models.CharField(max_length = 255 , help_text = '.....', null=True)
    meta_keywords = models.CharField(max_length = 255 , help_text='.....' ,null=True)
    
    def __str__(self):
        return self.name
    class Meta : 
        ordering = ['-pubdate']
    def get_absolute_url(self):
        return reverse('show_product', args=[self.slug])   
        
class Client(models.Model):
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta :
        pass
       
class Order(models.Model):
    itm =models.ForeignKey(Item , on_delete=models.CASCADE)
    ship_to = models.CharField(max_length=100)
    orderdate = models.DateTimeField(auto_now = True )

    class Meta :  
        ordering = ['-orderdate']
    def __str__(self):
        return  str(self.itm) + ' by ' + str(self.clt) + '  AT : ' +str(self.orderdate)


def signal_receiver(sender ,instance , *args , **kwargs):
    slug = slugify(instance.name)
    instance.slug = slug
    
pre_save.connect(signal_receiver , sender=Item)
pre_save.connect(signal_receiver , sender=Categorie)



