from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from .models import Favorite
from salon_shop.models import Product


def get_favorite_list(user):
    return Favorite.objects.get_queryset().filter(user=user)


def favorite_add(request, pk):
    user = auth.get_user(request)
    product = get_object_or_404(Product, id=pk)
    Favorite.objects.get_or_create(user=user, product=product)
    return render(request, 'favorite.html', {'favorite_list': get_favorite_list(user)})


def favorite_remove(request, pk):
    user = auth.get_user(request)
    product = get_object_or_404(Product, id=pk)
    Favorite.objects.filter(user=user, product=product).delete()
    return render(request, 'favorite.html', {'favorite_list': get_favorite_list(user)})


def favorite_detail(request):
    user = auth.get_user(request)
    return render(request, 'favorite.html', {'favorite_list': get_favorite_list(user)})


def favorite_list(request):
    user = auth.get_user(request)
    return render(request, 'favorite_list.html', {'favorite_list': get_favorite_list(user)})