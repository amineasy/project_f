# Generated by Django 4.2.4 on 2025-03-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0029_productitem_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='option_groups',
            field=models.ManyToManyField(related_name='option_groups', to='catalog.optiongroup'),
        ),
    ]
