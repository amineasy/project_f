# Generated by Django 4.2.4 on 2025-03-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('slug', models.SlugField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
