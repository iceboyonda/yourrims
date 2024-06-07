from django.views.generic import ListView
from .models import *
from django.shortcuts import redirect, render


class RimsView(ListView):
    model = Rims
    paginate_by = 4
    template_name = 'blog/rims.html'
    context_object_name = 'rims'


class SparesView(ListView):
    model = Spares
    paginate_by = 4
    template_name = 'blog/spares.html'
    context_object_name = 'spares'


def index_view(request):
    return render(request, 'blog/index.html')


def cart_add(request, rims_id):
    if request.method == 'POST':
        rims = Rims.objects.get(id=rims_id)
        carts = Cart.objects.filter(user=request.user, rims=rims)

        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(user=request.user, rims=rims, quantity=1)

    return redirect('cart')


def get_cart(request):
    rims_cart = Cart.objects.filter(user=request.user, rims__isnull=False)
    spares_cart = Cart.objects.filter(user=request.user, spares__isnull=False)
    context = {
        'rims_cart': rims_cart,
        'spares_cart': spares_cart
    }
    return render(request, 'blog/cart.html', context)


def delete_card(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect('cart')


def spares_add_to_cart(request, spare_id):
    if request.method == 'POST':
        spare = Spares.objects.get(id=spare_id)
        cart = Cart.objects.filter(user=request.user, spares=spare)

        if cart.exists():
            carts = cart.first()
            carts.quantity += 1
            carts.save()
        else:
            Cart.objects.create(user=request.user, spares=spare, quantity=1)
    return redirect('cart')




