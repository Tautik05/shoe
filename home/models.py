from django.db import models
from accounts.models import *

#Create your models here.

class Shoes(models.Model):
    
    shoe_name = models.CharField(max_length=100)
    shoe_description = models.CharField(max_length=100)
    shoe_price = models.IntegerField()
    shoe_image = models.ImageField(upload_to="img")


    def __str__(self):
        return self.shoe_name



class CartItem(models.Model):
    # user = models.ForeignKey(Consumer,on_delete=models.SET_NULL, null=True , blank=True)
    shoe = models.ForeignKey(Shoes, related_name='items',on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    complete=models.IntegerField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)




    


    






    











    