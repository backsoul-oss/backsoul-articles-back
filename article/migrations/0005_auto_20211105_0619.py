# Generated by Django 3.2.8 on 2021-11-05 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('article', '0004_auto_20211105_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='category.Category'),
        ),
    ]
