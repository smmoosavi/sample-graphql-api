import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name')


class UserQuery:
    me = graphene.Field(UserType)

    def resolve_me(self, info, **kwargs):
        user = info.context.user
        if user.is_authenticated:
            return user
        return None
