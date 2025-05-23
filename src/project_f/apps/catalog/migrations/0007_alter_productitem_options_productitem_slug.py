# Generated by Django 4.2.4 on 2025-03-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_productitem_created_by_productitem_created_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productitem',
            options={'verbose_name': 'ProductItem', 'verbose_name_plural': 'Product Items'},
        ),
        migrations.AddField(
            model_name='productitem',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=None, unique=True),
            preserve_default=False,
        ),
    ]
