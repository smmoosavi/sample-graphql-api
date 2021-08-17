from django.db.models import Q

from posts.models import Post


def get_all_posts(*, viewer):
    return Post.objects.filter(Q(published=True) | Q(author=viewer))
