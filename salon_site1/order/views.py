from django.contrib import auth
from django.shortcuts import render
from .models import OrderItem, Order
from salon_shop.models import Product
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):

    """Проверка формы на валидность и создание заказа """
    cart = Cart(request)

    if request.method == 'POST':
        user = auth.get_user(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.user = user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],)

            cart.clear()
            return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'order/create.html', {'cart': cart, 'form': form})


def history_orders(request):

    """ Вывод истории заказов пользователя """

    user = auth.get_user(request)
    history_list = Order.objects.get_queryset().filter(user_id=user.id)
    return render(request, 'order/history_orders.html',  {'history_list': history_list})


def list_order_item(request, order_id):

    """Вывод списка товаров в заказе"""

    list_order_items = OrderItem.objects.get_queryset().filter(order_id=order_id)
    list_prod_in_ord = []
    for item in list_order_items:
        product = Product.objects.get(id=item.product_id)
        prod_dict = {
            'id': product.id,
            'image': product.image,
            'name': product.name,
            'coast': item.price,
            'quantity': item.quantity
                     }
        list_prod_in_ord.append(prod_dict)
    return render(request, 'order/list_order_item.html', {'list_prod_in_ord': list_prod_in_ord})

