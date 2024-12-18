# Generated by Django 5.0.7 on 2024-07-23 15:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(default='', null=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='CarForRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('engine_type', models.CharField(blank=True, max_length=100, null=True)),
                ('seater', models.IntegerField(default=5)),
                ('car_model', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manuel', 'Manuel')], default='Automatic', max_length=100)),
                ('drive_type', models.CharField(choices=[('Self Drive', 'Self Drive'), ('With a Driver', 'With a Driver')], default='With a Driver', max_length=100)),
                ('color', models.CharField(blank=True, default='Black', max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='car_for_rent')),
                ('accra_price', models.CharField(max_length=10)),
                ('outside_price', models.CharField(max_length=10)),
                ('just_accra', models.BooleanField(default=False)),
                ('outside_accra', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='rental.category')),
            ],
            options={
                'verbose_name_plural': 'Cars For Rent',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='FeaturedCarForRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('engine_type', models.CharField(blank=True, max_length=100, null=True)),
                ('seater', models.IntegerField(default=5)),
                ('car_model', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manuel', 'Manuel')], default='Automatic', max_length=100)),
                ('drive_type', models.CharField(choices=[('Self Drive', 'Self Drive'), ('With a Driver', 'With a Driver')], default='With a Driver', max_length=100)),
                ('color', models.CharField(blank=True, default='Black', max_length=100, null=True)),
                ('image', models.ImageField(upload_to='car_for_rent')),
                ('accra_price', models.CharField(max_length=10)),
                ('outside_price', models.CharField(max_length=10)),
                ('just_accra', models.BooleanField(default=False)),
                ('outside_accra', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homevehicle', to='rental.category')),
            ],
            options={
                'verbose_name_plural': 'Featured Cars For Rent',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='NeedADriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up_location', models.CharField(max_length=100)),
                ('drop_off_location', models.CharField(max_length=100)),
                ('pick_up_date', models.CharField(blank=True, max_length=20, null=True)),
                ('drop_off_date', models.CharField(blank=True, max_length=20, null=True)),
                ('pick_up_time', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Need a driver',
                'ordering': ['-pick_up_date'],
            },
        ),
    ]
