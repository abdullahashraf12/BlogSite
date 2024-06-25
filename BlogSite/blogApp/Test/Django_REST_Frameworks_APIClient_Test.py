from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from userauths.models import User
from ..models import Post, Profile

class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='memo2@gmail.com',
            password='password123',
            email='memo2@gmail.com'
        )
        self.profile = Profile.objects.create(user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        url = reverse('blogApp:post-list-create')
        data = {
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'author': self.profile.id,  # Use the profile ID here
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_update_post(self):
        post = Post.objects.create(
            title='Test Post', 
            content='This is a test post content.', 
            author=self.profile
        )
        url = reverse('blogApp:post-detail', kwargs={'pk': post.id})
        updated_data = {
            'title': 'Updated Post',
            'content': 'Updated content.',
            'author': self.profile.id,  # Use the profile ID here
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.title, 'Updated Post')

    def test_delete_post(self):
        post = Post.objects.create(
            title='Test Post', 
            content='This is a test post content.', 
            author=self.profile
        )
        url = reverse('blogApp:post-detail', kwargs={'pk': post.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
