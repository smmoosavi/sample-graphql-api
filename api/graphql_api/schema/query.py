import graphene

from posts.schema.query import PostQuery


class Query(graphene.ObjectType, PostQuery):
    hello = graphene.String()

    def resolve_hello(self, info):
        return 'world'
