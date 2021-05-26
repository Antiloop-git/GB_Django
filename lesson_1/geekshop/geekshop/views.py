from django.shortcuts import render


def index(request):
    title = 'geekshop'

    context = {
        'title': title,
    }
    return render(request, 'index.html', context=context)

def contact(request):
    title = 'Контакты'

    context = {
        'title': title,
    }
    return render(request, 'contact.html', context=context)
