from django.shortcuts import render
from .forms import *
from products.models import *
from django.db.models import Count

def landing(request):
    """Генерирует страницу предварительного открытия с возможностью подписаться на рассылку"""
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.cleaned_data
        form.save()
    return render(request, 'landing/landing.html', locals())

def home(request):
    """Генерирует основную главную страницу сайта"""
    featured_products = Product.objects.filter(is_active = True)[:8] # TODO: можно добавить отдельно флаг в модель в продвигаемые продукты
    categories_count = Product.objects.values('category__name','category__image').filter(is_active = True).annotate(count = Count('id'))
    return render(request, 'landing/home.html', locals())