from django.shortcuts import render

from orders.models import ProductInBasket
from .models import *


def product(request, pk):

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_images = ProductImage.objects.filter(is_active = True, product__pk = pk)
    main_image = ProductImage.objects.get(is_main = True, product__pk = pk)
    product = Product.objects.get(pk=pk)
    try:
        nmb = ProductInBasket.objects.get(session_key = session_key, is_active = True, product_id = pk).nmb
    except: nmb = 0
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)
    print(session_key)
    return render(request, 'products/product.html', locals())
