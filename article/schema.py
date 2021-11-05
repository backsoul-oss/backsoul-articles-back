# schema graphql list articles
import graphene
from graphene_django.types import DjangoObjectType
from .models import Article
from django.db.models import Q
from graphene import String, List
from graphene_django.converter import convert_django_field
from graphene import ObjectType, String, Int
from category.schema import CategoryType
@convert_django_field.register(Article)
def convert_field_to_string(field, registry=None):
    return List(String, source='get_articles')

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class Query(graphene.AbstractType):
    all_articles = graphene.List(ArticleType, search_title=graphene.String(),
                                 first=graphene.Int(),
                                 skip=graphene.Int(),)
    
    article_by_slug = graphene.Field(ArticleType, _slug=graphene.String())
    
    def resolve_article_by_slug(self, info, _slug=None, **kwargs):
        return Article.objects.all().filter(_slug=_slug)[0]

    def resolve_all_articles(self, info, search_title=None, first=None, skip=None, **kwargs):
        articles = Article.objects.all()
        if search_title:
            articles = Article.objects.all().filter(title=search_title)

        if skip:
            articles = articles[skip:]

        if first:
            articles = articles[:first]
        return articles
