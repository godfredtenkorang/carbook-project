# Generated by Django 5.0.7 on 2024-07-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_featuredbooking_car_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredbooking',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
