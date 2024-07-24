from django.shortcuts import render
from .models import *

# Create your views here.
# def home(request):
#     return render(request, 'home.html')



def shoe(request):
    queryset = Shoes.objects.all()
    context = {'sneakers': queryset}
    return render(request, 'home.html', context)


def product_page(request, id):

    queryset = Shoes.objects.get(id=id)
    context ={'sneaker': queryset}
    return render(request, 'product.html', context)



# def cart_page(request):

   
#     return render(request, 'cart.html')


# def add_to_cart(request, id):
    


