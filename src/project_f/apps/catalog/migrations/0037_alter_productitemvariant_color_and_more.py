# Generated by Django 4.2.4 on 2025-03-28 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0036_alter_productitemvariant_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitemvariant',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.color'),
        ),
        migrations.AlterField(
            model_name='productitemvariant',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.size'),
        ),
    ]
