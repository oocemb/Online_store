# Generated by Django 4.0.2 on 2022-02-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productcategory_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=True),
        ),
    ]