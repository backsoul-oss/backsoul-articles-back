# Generated by Django 3.2.8 on 2021-11-01 23:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_remove_article_text_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
