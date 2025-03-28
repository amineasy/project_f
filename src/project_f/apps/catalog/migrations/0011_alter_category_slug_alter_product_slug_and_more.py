# Generated by Django 4.2.4 on 2025-03-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_product_slug_alter_productitem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
    ]
