# Generated by Django 4.2.4 on 2025-03-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_remove_productattribute_option_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
