import graphene

from users.schema.user_mutations import UserMutations


class Mutation(graphene.ObjectType, UserMutations):
    pass
