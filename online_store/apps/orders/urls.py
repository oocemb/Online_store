from django.urls import path, include
from .views import *

app_name = "orders"
urlpatterns = [

    path('checkout_payments/', checkout_payments,  name='checkout_payments'),
    path('checkout_details/', checkout_details,  name='checkout_details'),
    path('basket_adding/', basket_adding,  name='basket_adding'),
    path('cart/', cart_detail,  name='cart_detail'),

]
