from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='hidden')
        cls.published_post = Post.objects.create(
            title='some pub title',
            text='some pub text',
            status='pub',
            author=cls.user,
        )
        cls.draft_post = Post.objects.create(
            title='some drf title',
            text='some drf text',
            status='draft',
            author=cls.user,
        )

    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_blogs_url(self):
        response = self.client.get('/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_blogs_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_show_post_published_in_posts_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.published_post.title)
        self.assertContains(response, self.published_post.text)

    def test_not_show_post_draft_in_posts_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertNotContains(response, self.draft_post.title)
        self.assertNotContains(response, self.draft_post.text)

    def test_post_detail_url(self):
        response = self.client.get(f'/blogs/{self.published_post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.published_post.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_published_detail_content(self):
        response = self.client.get(reverse('post_detail', args=[self.published_post.id]))
        self.assertContains(response, self.published_post.title)
        self.assertContains(response, self.published_post.author)
        self.assertContains(response, self.published_post.text)

    def test_post_draft_detail_content(self):
        response = self.client.get(reverse('post_detail', args=[self.draft_post.id]))
        self.assertContains(response, self.draft_post.title)
        self.assertContains(response, self.draft_post.author)
        self.assertContains(response, self.draft_post.text)

    def test_post_create_url(self):
        response = self.client.get(f'/blogs/create/')
        self.assertEqual(response.status_code, 200)

    def test_post_create_url_by_name(self):
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)

    def test_post_create(self):
        response = self.client.post(
            reverse('post_create'),
            {
                'title': 'some pub create title',
                'text': 'some pub create text',
                'status': 'pub',
                'author': self.user.id,
            },

        )

        self.assertEqual(response.status_code, 302)

    def test_post_update_url(self):
        response = self.client.get(f'/blogs/update/{self.published_post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_update_url_by_name(self):
        response = self.client.get(reverse('post_update', args=[self.published_post.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_published_update(self):
        response = self.client.post(
            reverse('post_update', args=[self.published_post.id]),
            {
                'title': 'some pub up title',
                'text': 'some pub up text',
                'status': 'pub',
                'author': self.user.id,
            },
            )

        self.assertEqual(response.status_code, 302)

    def test_post_delete_url(self):
        response = self.client.get(f'/blogs/delete/{self.published_post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_delete_url_by_name(self):
        response = self.client.get(reverse('post_delete', args=[self.published_post.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_delete(self):
        response = self.client.post(reverse('post_delete', args=[self.draft_post.id]))
        self.assertEqual(response.status_code, 302)
