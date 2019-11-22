from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User

Category_Choice=(
    ('sh','shoe'),
    ('ha','hat'),
    ('wa','watch'),
)

class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True, null=True)
    category=models.CharField(choices=Category_Choice,max_length=3 ,default='shoe')
    slug=models.SlugField(default='shoe')
    description=models.TextField()
    on_stock=models.IntegerField(default=1)
    item_make=models.CharField(blank=True,null=True,max_length=100)
    image=models.ImageField(default='item.jpg',upload_to='item_images/')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('webapp:product',kwargs={ 'slug':self.slug})    
    
    def get_add_to_cart_url(self,slug):
        return reverse('webapp:add_to_cart',slug=self.slug)       

 

class OrderItem(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return self.item.title


class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered=models.BooleanField(default=False)
    # ordered_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return self.user.username

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='item.jpg',upload_to='profile_images/')


    def __str__(self):
        return (self.user.username)
    


