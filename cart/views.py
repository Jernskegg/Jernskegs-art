'''Create your views here.'''
from django.shortcuts import render, redirect


def get_cart(request):
    ''' A view that will enable viewing the shopping cart '''
    return render(request, 'cart.html')


def add_to_cart(request, item_id):
    ''' Adds an item to the cart'''

    cart = request.session.get('cart', [])

    if int(item_id) not in cart:
        print(cart)
        cart.append(int(item_id))
        request.session['cart'] = cart
        return redirect('gallery')
    else:
        return redirect('gallery')
