from django.shortcuts import render, get_object_or_404
from .models import Category, Product, News
from django.http import HttpResponseNotFound, HttpResponse


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'salon_shop/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'salon_shop/detail.html', {'product': product})


def about(request):
    return render(request, "salon_shop/about.html", {'title':'О магазине'})


def base(request):
    return render(request, "salon_shop/index_base.html", {'title':'Интернет-магазин'})


def index(request):
    return render(request, "salon_shop/index.html", {'title':'Главная страница'})


def new_in(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': "Новости, скидки,акции"

    }
    return render(request, 'salon_shop/news.html', context=context )


def pr(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'title':'Продукция'
    }
    return render(request, 'salon_shop/product.html', context=context)


def login(request):
    return render(request, 'salon_shop/ajax/login_popup.html', {'title':'Войти'})


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи= {post_id}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Ошибка 404</h2>,\n <h1>Страница не найдена</h1>'
                                ',\n<h3>Проверьте, правильно ли Вы ввели адрес. Правильно?\nТогда, '
                                'возможно, на странице идут технические работы</h3>')

