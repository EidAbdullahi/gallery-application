# Generated by Django 3.1 on 2021-01-10 17:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20210110_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
