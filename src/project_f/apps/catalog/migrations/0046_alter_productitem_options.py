# Generated by Django 4.2.4 on 2025-03-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0045_productclass_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='options',
            field=models.ManyToManyField(blank=True, to='catalog.optiongroupvalue'),
        ),
    ]
