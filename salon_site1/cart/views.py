from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_POST
from salon_shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):

    """Добавление товара в корзину"""

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    return redirect('cart:cart_detail')


def cart_remove(request, product_id):

    """Удаление товара из корзины"""

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):

    """Список товаров в корзине"""

    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart':cart})


def cart_clear(request):
    del request.session['cart']
    request.session.modified = True
    return HttpResponseRedirect("/cart")




