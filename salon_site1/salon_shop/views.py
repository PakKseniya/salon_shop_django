from django.shortcuts import render, get_object_or_404
from .models import Category, Product, News
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from cart.forms import CartAddProductForm
from favorites.views import favorite_list


def product_list(request, category_slug=None):

    """Получение списка товаров по категории """

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'salon_shop/product_list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products,
                      'cart_product_form': cart_product_form
                  })


def product_detail(request, slug):

    """Получение детальной информации по товару"""

    product = get_object_or_404(Product,  slug=slug,  available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'salon_shop/product_detail.html', {'product': product,
                                                              'cart_product_form': cart_product_form})


def pr(request):

    """Получение списка товаров"""

    products = Product.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'products': products,
        'title':'Продукция',
        'cart_product_form': cart_product_form,
    }
    return render(request, 'salon_shop/product_list.html', context=context)


def about(request):

    """информация о магазине"""

    return render(request, "salon_shop/about.html")


def base(request):
    return HttpResponseRedirect("/index/")


def index(request):
    """Вывод главной страницы"""

    return render(request, "salon_shop/index.html", {'title':'Главная страница'})


def new_in(request):

    """Вывод списка новостей"""

    news = News.objects.all()
    context = {
        'news': news,
        'title': "Новости, скидки,акции"

    }
    return render(request, 'salon_shop/news.html', context=context)


def salon_kr(request):
    return render(request, 'salon_shop/salon_kr.html', {'title':" О салоне красоты"})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Ошибка 404</h2>,\n <h1>Страница не найдена</h1>'
                                ',\n<h3>Проверьте, правильно ли Вы ввели адрес. Правильно?\nТогда, '
                                'возможно, на странице идут технические работы</h3>')

