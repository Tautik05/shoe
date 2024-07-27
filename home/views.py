from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.http import JsonResponse




def shoe(request):
    queryset = Shoes.objects.all()
    context = {'sneakers': queryset}
    return render(request, 'home.html', context)


def product_page(request, id):

    queryset = Shoes.objects.get(id=id)
    context ={'sneaker': queryset}
    return render(request, 'product.html', context)





# def add_to_cart(request, shoe_id):
#     if 'consumer_id' not in request.session:
#         messages.error(request, 'You need to log in to add items to the cart.')
#         return redirect('/login')

#     shoe = get_object_or_404(Shoes, id=shoe_id)
#     cart = request.session.get('cart', [])
    
#     # Check if the shoe is already in the cart
#     for item in cart:
#         if item['shoe_id'] == shoe_id:
#             item['quantity'] += 1
#             break
#     else:
#         cart.append({'shoe_id': shoe_id, 'quantity': 1, 'shoe_name': shoe.shoe_name, 'shoe_price': shoe.shoe_price, 'shoe_image': shoe.shoe_image.url})


#     request.session['cart'] = cart
#     messages.success(request, 'Item added to cart successfully!')
#     return redirect('view_cart')

 



# def buy_shoe(request, id):
#     shoe = get_object_or_404(Shoes, id=id)
#     quantity_to_buy = int(request.POST.get('quantity'))  # Assuming quantity is passed via POST

#     if shoe.stock >= quantity_to_buy:
#         shoe.stock -= quantity_to_buy
#         shoe.save()
#         # You could add additional logic here to create an order, process payment, etc.
#         return redirect('success_page')  # Redirect to a success page or order confirmation
#     else:
#         return redirect('out_of_stock_page')  # Redirect to a page indicating out of stock










# def add_to_cart(request, shoe_id):
#     if not request.user.is_authenticated:
#         messages.error(request, 'You need to log in to add items to the cart.')
#         return redirect('/login')

#     shoe = get_object_or_404(Shoes, id=shoe_id)
#     quantity_to_buy = int(request.POST.get('quantity', 1))


#     if shoe.stock >= quantity_to_buy:
#         shoe.stock-=quantity_to_buy
#         shoe.save()
#         cart_item, created = CartItem.objects.get_or_create(user=request.user, shoe=shoe, complete=False)

#         if not created:
#         # If the item was already in the cart, increment the quantity
#           cart_item.quantity += 1
          
#         else:
#         # Optionally handle the case where a new item was created
#           cart_item.quantity = 1

#         cart_item.save()

#         messages.success(request, 'Item added to cart successfully!')
#         return redirect('view_cart')


#     else:
#        messages.error(request, 'Not enough stock available.')
#        return redirect('product_page', id=shoe_id) 


# def add_to_cart(request, shoe_id):
#     if not request.user.is_authenticated:
#         messages.error(request, 'You need to log in to add items to the cart.')
#         return redirect('/login')

#     shoe = get_object_or_404(Shoes, id=shoe_id)
#     quantity_to_buy = int(request.POST.get('quantity', 1))
#     cart_item, created = CartItem.objects.get_or_create(user=request.user, shoe=shoe, complete=False)

#     if created:
#         # If the item was not in the cart, create it with the specified quantity
#         if shoe.stock >= quantity_to_buy:
#             shoe.stock -= quantity_to_buy
#             shoe.save()
#             cart_item.quantity = quantity_to_buy
#             cart_item.save()
#         else:
#             messages.error(request, 'Not enough stock available.')
#             return redirect('view_cart')
#     else:
#         new_quantity = cart_item.quantity + quantity_to_buy
#         if new_quantity > 0 and shoe.stock >= quantity_to_buy:
#             shoe.stock -= quantity_to_buy
#             shoe.save()
#             cart_item.quantity = new_quantity
#             cart_item.save()
#         elif new_quantity <= 0:
#             shoe.stock += cart_item.quantity  # Restore stock before deleting item
#             shoe.save()
#             cart_item.delete()
#         else:
#             messages.error(request, 'Not enough stock available.')
#             return redirect('view_cart')

#     messages.success(request, 'Cart updated successfully!')
#     return redirect('view_cart')





def add_to_cart(request, shoe_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to log in to add items to the cart.')
        return redirect('/login')

    shoe = get_object_or_404(Shoes, id=shoe_id)
    quantity_to_add = int(request.POST.get('quantity', 1))
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, shoe=shoe)
    
    if created:
        if shoe.stock >= quantity_to_add:
            shoe.stock -= quantity_to_add
            shoe.save()
            cart_item.quantity = quantity_to_add
            cart_item.save()
        else:
            messages.error(request, 'Not enough stock available.')
            return redirect('view_cart')
    else:
        new_quantity = cart_item.quantity + quantity_to_add
        if new_quantity > 0 and shoe.stock >= quantity_to_add:
            shoe.stock -= quantity_to_add
            shoe.save()
            cart_item.quantity = new_quantity
            cart_item.save()
        elif new_quantity <= 0:
            shoe.stock += cart_item.quantity
            shoe.save()
            cart_item.delete()
        else:
            messages.error(request, 'Not enough stock available.')
            return redirect('view_cart')

    messages.success(request, 'Cart updated successfully!')
    return redirect('view_cart')







# def view_cart(request):

#     if not request.user.is_authenticated:
#         messages.error(request, 'You need to log in to view your cart.')
#         return redirect('/login')

#     cart_items = CartItem.objects.filter(user=request.user, complete=False)
    
#     context = {
#         'cart': cart_items,
#     }
    
#     return render(request, 'cart.html', context)




def view_cart(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to log in to view your cart.')
        return redirect('/login')

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    
    return render(request, 'cart.html', context)






def clear_cart(request):
    request.session['cart'] = []
    messages.success(request, 'Cart cleared.')
    return redirect('view_cart')




