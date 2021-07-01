def product(request):
    print('context_processors product')

    s = 'Product is good'
    return {
        'product_test': s
    }
