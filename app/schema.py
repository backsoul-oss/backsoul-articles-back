import graphene
import article.schema


class Query(article.schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)
