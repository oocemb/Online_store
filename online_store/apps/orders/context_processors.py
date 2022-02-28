from products.models import ProductImage
from .models import *


def getting_basket_info(request):

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    basket = ProductInBasket.objects.filter(session_key = session_key, is_active=True)
    prod_total_nmb = basket.count()
    total_basket_price = sum(prod.total_amount for prod in basket)
    

    return locals()