from django.contrib.auth.models import User
from django.test import TestCase

from posts.interactors import get_all_posts
from posts.models import Post


class PostsTestCase(TestCase):
    def setUp(self) -> None:
        self.u1 = User.objects.create_user(username='user1')
        self.u2 = User.objects.create_user(username='user2')
        self.p1 = Post(
            title="post 1", body="body 1", author=self.u1, published=True)
        self.p1.save()
        self.p2 = Post(
            title="draft 2", body="body 2", author=self.u1, published=False)
        self.p2.save()

    def test_get_all_posts_by_author(self):
        ps_u1 = get_all_posts(viewer=self.u1)
        self.assertTrue(len(ps_u1) == 2)
        self.assertTrue(self.p1 in ps_u1)
        self.assertTrue(self.p2 in ps_u1)

    def test_get_all_posts_by_others(self):
        ps_u2 = get_all_posts(viewer=self.u2)
        self.assertTrue(len(ps_u2) == 1)
        self.assertTrue(self.p1 in ps_u2)
        self.assertTrue(self.p2 not in ps_u2)
