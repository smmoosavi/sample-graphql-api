import graphene
from graphene_django import DjangoObjectType

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
