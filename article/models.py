from django.db import models

from category.models import Category
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Article(models.Model):
    title = models.CharField(max_length=200)
    _slug = models.CharField(max_length=200, default='_slug')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', blank=True)
    text_description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=0)
