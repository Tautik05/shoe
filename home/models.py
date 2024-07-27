from django.db import models
from accounts.models import *

#Create your models here.

class Shoes(models.Model):
    
    shoe_name = models.CharField(max_length=100)
    shoe_description = models.CharField(max_length=100)
    shoe_price = models.IntegerField()
    shoe_image = models.ImageField(upload_to="img")
    stock=models.IntegerField(default=0)


    def __str__(self):
        return self.shoe_name



class Cart(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.username}"
    
    @property
    def total_amount(self):
        total = sum(item.quantity * item.shoe.shoe_price for item in self.items.all())
        return total







class CartItem(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoes, related_name='items',on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    complete=models.IntegerField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)






    @property
    def shoe_name(self):
        return self.shoe.shoe_name

    @property
    def shoe_price(self):
        return self.shoe.shoe_price

    @property
    def shoe_image(self):
        return self.shoe.shoe_image.url

    








    











    