from django.urls import path, include
from .views import *


app_name = "landing"
urlpatterns = [
    path('', home,  name='home'),
    path('landing/', landing,  name='landing'),
]
