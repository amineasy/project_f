# Generated by Django 4.2.4 on 2025-03-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_alter_productclass_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productclass',
            name='options',
            field=models.ManyToManyField(blank=True, to='catalog.option'),
        ),
    ]
