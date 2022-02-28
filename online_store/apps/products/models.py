from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64,blank=True, null=True, default=None)
    image = models.ImageField(upload_to='static/image/category_images/', blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return "%s" % (self.name)
    
    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товара'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete= models.DO_NOTHING)
    main_image = models.ImageField(upload_to='static/image/products_images/', blank=True, null=True, default=None)
    name = models.CharField(max_length=128,blank=True, null=True, default=None)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return "%s %s" % (self.name, self.price)
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete = models.SET_NULL)
    image = models.ImageField(upload_to='static/image/products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return "%s" % self.id
    
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
