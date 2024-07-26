from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib import messages





def shoe(request):
    queryset = Shoes.objects.all()
    context = {'sneakers': queryset}
    return render(request, 'home.html', context)


def product_page(request, id):

    queryset = Shoes.objects.get(id=id)
    context ={'sneaker': queryset}
    return render(request, 'product.html', context)





def add_to_cart(request, shoe_id):
    if 'consumer_id' not in request.session:
        messages.error(request, 'You need to log in to add items to the cart.')
        return redirect('/login')

    shoe = get_object_or_404(Shoes, id=shoe_id)
    cart = request.session.get('cart', [])
    
    # Check if the shoe is already in the cart
    for item in cart:
        if item['shoe_id'] == shoe_id:
            item['quantity'] += 1
            break
    else:
        cart.append({'shoe_id': shoe_id, 'quantity': 1, 'shoe_name': shoe.shoe_name, 'shoe_price': shoe.shoe_price, 'shoe_image': shoe.shoe_image.url})


    request.session['cart'] = cart
    messages.success(request, 'Item added to cart successfully!')
    return redirect('view_cart')

 

# from .models import Shoes, CartItem

# def add_to_cart(request, shoe_id):
#     shoe = get_object_or_404(Shoes, id=shoe_id)
#     cart = request.session.get('cart', [])
    
#     # Check if the item is already in the cart
#     if shoe_id in cart:
#         # Update quantity if item is already in the cart
#         cart_item = CartItem.objects.get(shoe=shoe, complete=False)
#         cart_item.quantity += 1
#         cart_item.save()
#     else:
#         # Add new item to the cart
#         cart.append(shoe_id)
#         request.session['cart'] = cart
    
#     messages.success(request, 'Item added to cart successfully!')
#     return redirect('view_cart')  # or redirect to the desired page




# from django.shortcuts import get_object_or_404, redirect
# from django.contrib import messages
# from .models import Shoes

# def add_to_cart(request, shoe_id):
#     if 'consumer_id' not in request.session:
#         messages.error(request, 'You need to log in to add items to the cart.')
#         return redirect('/login')

#     shoe = get_object_or_404(Shoes, id=shoe_id)
#     cart = request.session.get('cart', [])
    
#     # Debug: Print the cart contents before modification
#     print("Cart before adding:", cart)

#     # Ensure that each item in the cart is a dictionary
#     for item in cart:
#         if isinstance(item, int):
#             # Convert integer items to dictionary format
#             cart.remove(item)
#             cart.append({'shoe_id': item, 'quantity': 1})

#     # Check if the shoe is already in the cart
#     for item in cart:
#         if item['shoe_id'] == shoe_id:
#             item['quantity'] += 1
#             break
#     else:
#         cart.append({'shoe_id': shoe_id, 'quantity': 1, 'shoe_name': shoe.shoe_name, 'shoe_price': shoe.shoe_price, 'shoe_image': shoe.shoe_image.url})

#     request.session['cart'] = cart

#     # Debug: Print the cart contents after modification
#     print("Cart after adding:", cart)

#     messages.success(request, 'Item added to cart successfully!')
#     return redirect('view_cart')




def view_cart(request):
    cart = request.session.get('cart', [])
    print(cart)  # Debug print statement
    context = {'cart': cart}
    return render(request, 'cart.html', context)



def clear_cart(request):
    request.session['cart'] = []
    messages.success(request, 'Cart cleared.')
    return redirect('view_cart')
