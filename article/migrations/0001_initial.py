# Generated by Django 3.2.8 on 2021-11-01 16:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('_slug', models.CharField(default='SOME STRING', max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('text_description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='image', upload_to='image')),
                ('category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
