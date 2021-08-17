import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType

from posts.interactors import get_all_posts
from posts.models import Post, Comment


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'text', 'author')


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author')

    comments = graphene.List(graphene.NonNull(CommentType), required=True)

    def resolve_comments(self, info):
        return self.comments.all()


class PostQuery:
    post = graphene.Field(PostType, id=graphene.Argument(graphene.ID, required=True))

    def resolve_post(self, info, **kwargs):
        post_id = kwargs.get('id')
        try:
            return Post.objects.get(id=post_id)
        except:
            return None

    posts = graphene.List(graphene.NonNull(PostType), required=True)

    def resolve_posts(self, info, **kwargs):
        user = info.context.user
        return get_all_posts(viewer=user)
