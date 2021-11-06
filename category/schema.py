
import graphene
from graphene_django.types import DjangoObjectType
from .models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(graphene.AbstractType):
    categories = graphene.List(CategoryType)

    category_by_id = graphene.Field(CategoryType, id=graphene.Int())

    def resolve_category_by_id(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Category.objects.get(pk=id)
        return None

    def resolve_categories(self, info, **kwargs):
        categories = Category.objects.all()
        return categories
