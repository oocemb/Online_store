from django.urls import path, include
from .views import *

app_name = "product"
urlpatterns = [

    path('product/<pk>/', product,  name='product'),

]
