import graphene
import article.schema
import category.schema


class Query(category.schema.Query, article.schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)
