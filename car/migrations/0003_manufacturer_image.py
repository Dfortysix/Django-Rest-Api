# Generated by Django 5.0.6 on 2024-06-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_manufacturer_remove_car_color_car_body_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/manufaturers'),
        ),
    ]
