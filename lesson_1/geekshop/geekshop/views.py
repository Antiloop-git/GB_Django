from django.shortcuts import render

def index(request):
    title = 'geekshop'

    links_product = [
        {'href': 'index', 'url': 'static/img/product-1.jpg'},
        {'href': 'index', 'url': 'static/img/product-2.jpg'},
        {'href': 'index', 'url': 'static/img/product-3.jpg'},
        {'href': 'index', 'url': 'static/img/product-4.jpg'},
    ]
    context = {
        'links_product': links_product,
        'title': title,
    }

    return render(request, 'index.html', context=context)

def contact(request):
    title = 'Контакты'

    context = {
        'title': title,
    }
    return render(request, 'contact.html', context=context)
