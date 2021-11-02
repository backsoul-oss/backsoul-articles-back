from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.core import serializers
from category.models import Category
from django.http import JsonResponse
from django.forms.models import model_to_dict


def index(request):
    articles = list(Article.objects.select_related().values())
    count = Article.objects.count()
    articles_list = []
    for article in articles:
        article = article
        article['image'] = article['image'].get_prep_value()
        articles_list.append(article)

    return JsonResponse({'articles': articles_list, 'count': count})


def article(request, _slug):
    return JsonResponse({'article': list(Article.objects.filter(_slug=_slug).values())[0]})
