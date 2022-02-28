from django.shortcuts import render
from .forms import *
from products.models import *
from django.db.models import Count

def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.cleaned_data
        #print(form)
        form.save()
    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active = True, is_main = True)[:8]
    categories_count = Product.objects.values('category__name','category__image').filter(is_active = True).annotate(count = Count('id'))
    return render(request, 'landing/home.html', locals())