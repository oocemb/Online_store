from django.db.models.signals import post_save
from django.db import models
from products.models import Product
from django.contrib.auth.models import User



class Status(models.Model):
    name = models.CharField(max_length=24,blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return "Статус № %s" % self.name
    
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=False, on_delete = models.DO_NOTHING)
    total_price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    customer_name = models.CharField(max_length=64,blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_adress = models.CharField(max_length=128,blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete = models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return "Заказ № %s %s" % (self.id, self.status.name)
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args,**kwargs):

        super(Order, self).save(*args,**kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete = models.SET_NULL)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    total_amount = models.DecimalField(decimal_places=2, max_digits=20, default=0) # price * nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return "%s" % self.product.name
    
    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args,**kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_amount = self.nmb * price_per_item

        super(ProductInOrder, self).save(*args,**kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs): # действия для других моделей чтоб не было цикла для данной
    order = instance.order
    order_total_price = 0
    all_product_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    
    for item in all_product_in_order:
        order_total_price += item.total_amount
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=40) # 40 максимум символов
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete = models.SET_NULL)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    total_amount = models.DecimalField(decimal_places=2, max_digits=20, default=0) # price * nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return "%s" % self.product.name
    
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args,**kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_amount = int(self.nmb) * price_per_item

        super(ProductInBasket, self).save(*args,**kwargs)
    