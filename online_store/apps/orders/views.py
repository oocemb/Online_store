from django.http import JsonResponse
from django.shortcuts import render

from products.models import ProductImage
from .models import *
from django.contrib.auth.models import User
# from django.contrib.sessions.backends.db import SessionStore

def basket_adding(request):

    # s = SessionStore()
    # s['last_login'] = 1376587691
    # s.create()
    # print(s.session_key)

    return_dict = dict()
    session_key = request.session.session_key

    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    is_delete = data.get("is_delete")

    if is_delete == "true":
        ProductInBasket.objects.filter(session_key=session_key, id=product_id).update(is_active=False)    
    else:
        new_prod, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, is_active=True, defaults={"nmb":nmb}) 
        if not created:
            new_prod.nmb += int(nmb)
            new_prod.save(force_update=True)

    prod_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)     
    prod_total_nmb = prod_in_basket.count()
    return_dict["prod_total_nmb"] = prod_total_nmb
    return_dict["total_basket_price"] = sum(prod.total_amount for prod in prod_in_basket)
    return_dict["products"] = list()

    for item in prod_in_basket:
        prod_dict = dict()
        prod_dict["id_prod"] = item.product.id
        prod_dict["category"] = item.product.category.name
        prod_dict["id_prod_basket"] = item.id
        prod_dict["image"] = ProductImage.objects.get(is_main = True, product__pk = item.product.id).image.url
        prod_dict["name"] = item.product.name
        prod_dict["price_per_item"] = item.price_per_item
        prod_dict["nmb"] = item.nmb
        return_dict["products"].append(prod_dict)

    return JsonResponse(return_dict)


def cart_detail(request):
    session_key = request.session.session_key
    prod_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)     
    if request.POST:
        print(request.POST)
        # if form.is_valid()
        # user, created = User.objects.get_or_create(username=)  
    return render(request, 'orders/cart_detail.html', locals())


def checkout_details(request):
    session_key = request.session.session_key
    prod_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)     
    if request.POST:
        print(request.POST)
    return render(request, 'orders/checkout_details.html', locals())


def checkout_payments(request):

    return render(request, 'orders/checkout_payments.html', locals())


