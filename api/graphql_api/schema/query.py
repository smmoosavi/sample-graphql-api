import graphene

from posts.schema.query import PostQuery
from users.schema.user_query import UserQuery


class Query(graphene.ObjectType, PostQuery, UserQuery):
    hello = graphene.String()

    def resolve_hello(self, info):
        return 'world'
