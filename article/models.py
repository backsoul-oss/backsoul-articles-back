from django.db import models

from category.models import Category
from django.utils import timezone
from cloudinary.models import CloudinaryField
from mdeditor.fields import MDTextField


class Article(models.Model):
    title = models.CharField(max_length=200)
    _slug = models.CharField(max_length=200, default='_slug')
    content = MDTextField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', blank=True)
    text_description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)
