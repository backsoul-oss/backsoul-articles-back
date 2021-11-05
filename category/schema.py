
import graphene
from graphene_django.types import DjangoObjectType
from .models import Category
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        

class Query(graphene.AbstractType):
    categories = graphene.List(CategoryType)
    
    def resolve_categories(self, info, **kwargs):
        categories = Category.objects.all()
        return categories