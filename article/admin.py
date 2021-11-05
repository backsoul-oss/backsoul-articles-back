from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'list_categories')
    list_filter = ('created_at', 'title')
    search_fields = ['title']
    
    def list_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all()])

admin.site.register(Article,ArticleAdmin)
