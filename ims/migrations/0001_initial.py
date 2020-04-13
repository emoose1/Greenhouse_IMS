# Generated by Django 3.0.5 on 2020-04-13 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200, verbose_name='Item Name')),
                ('item_availability', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='yes', max_length=3, verbose_name='Item Availability')),
                ('item_unique_identifier', models.CharField(blank=True, max_length=100, null=True, verbose_name='Item Serial/Unique ID #')),
                ('item_specs', models.TextField(blank=True, max_length=500, null=True, verbose_name='Item Specs')),
                ('checked_out_date', models.DateTimeField(auto_now=True, null=True)),
                ('checked_in_date', models.DateTimeField(auto_now=True, null=True)),
                ('checked_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Checked To User')),
                ('item_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ims.Category', verbose_name='Item Category')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ('item_name',),
            },
        ),
    ]
