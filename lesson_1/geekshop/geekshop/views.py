from django.shortcuts import render
from mainapp.models import Product

def index(request, pk=None):
    title = 'geekshop'
    products = Product.objects.all()[:4]

    context = {
        'products': products,
        'title': title,
    }

    return render(request, 'index.html', context=context)

def contact(request):
    title = 'Контакты'

    context = {
        'title': title,
    }
    return render(request, 'contact.html', context=context)
