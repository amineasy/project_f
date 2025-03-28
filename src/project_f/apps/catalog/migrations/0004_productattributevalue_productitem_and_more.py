# Generated by Django 4.2.4 on 2025-03-25 08:13

from django.db import migrations, models
import django.db.models.deletion
import project_f.libs.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_text', models.TextField(blank=True, null=True)),
                ('value_integer', models.IntegerField(blank=True, null=True)),
                ('value_float', models.FloatField(blank=True, null=True)),
                ('value_date', models.DateField(blank=True, null=True)),
                ('value_time', models.TimeField(blank=True, null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.productattribute')),
            ],
            options={
                'verbose_name': 'Attribute Value',
                'verbose_name_plural': 'Attribute Values',
            },
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('structure', models.CharField(choices=[('standalone', 'Standalone'), ('parent', 'Parent'), ('child', 'Child')], default='standalone', max_length=16)),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('upc', project_f.libs.db.fields.UppercaseCharField(blank=True, max_length=24, null=True, unique=True)),
                ('is_public', models.BooleanField(default=True)),
                ('meta_title', models.CharField(blank=True, max_length=128, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('attributes', models.ManyToManyField(through='catalog.ProductAttributeValue', to='catalog.productattribute')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.productitem')),
                ('product_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.product')),
            ],
            options={
                'verbose_name': 'ProductItem',
                'verbose_name_plural': 'ProductItems',
            },
        ),
        migrations.CreateModel(
            name='ProductRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveSmallIntegerField(default=0)),
                ('primary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_recommendation', to='catalog.productitem')),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.productitem')),
            ],
            options={
                'ordering': ('primary', '-rank'),
                'unique_together': {('primary', 'recommendation')},
            },
        ),
        migrations.AddField(
            model_name='productitem',
            name='recommended_product',
            field=models.ManyToManyField(blank=True, through='catalog.ProductRecommendation', to='catalog.productitem'),
        ),
        migrations.AddField(
            model_name='productattributevalue',
            name='product_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.productitem'),
        ),
        migrations.AddField(
            model_name='productattributevalue',
            name='value_multi_option',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.optiongroupvalue'),
        ),
        migrations.AddField(
            model_name='productattributevalue',
            name='value_option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attributes_related', to='catalog.optiongroupvalue'),
        ),
        migrations.AlterUniqueTogether(
            name='productattributevalue',
            unique_together={('product_item', 'attribute')},
        ),
    ]
