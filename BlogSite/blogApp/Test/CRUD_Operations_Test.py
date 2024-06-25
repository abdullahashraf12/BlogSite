from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from userauths.models import Profile
from ..models import Post

User = get_user_model()

class CRUDTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='memo@gmail.com', password='password123', email="memo@gmail.com")
        self.profile = Profile.objects.create(user=self.user)

    def test_create_post(self):
        self.client.force_login(self.user)
        url = reverse('blogApp:create_post')
        data = { 'author': self.profile  ,'title': 'Test Post', 'content': 'This is a test post.'}
        
        # Simulate posting data to create a post
        response = self.client.post(url, data)
        
        # Check that the response is a redirect (status code 302)
        expected_status_code = 302
        actual_status_code = response.status_code
        print(f"Expected status code: {expected_status_code}, Actual status code: {actual_status_code}")
        self.assertEqual(actual_status_code, expected_status_code)
        
        # Check that exactly one post has been created
        expected_post_count = 1
        actual_post_count = Post.objects.count()
        print(f"Expected post count: {expected_post_count}, Actual post count: {actual_post_count}")
        self.assertEqual(actual_post_count, expected_post_count)










    def test_update_post(self):
        self.client.force_login(self.user)
        post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.profile)
        url = reverse('blogApp:update_post', kwargs={'post_id': post.id})
        data = {'title': 'Updated Post', 'content': 'Updated content.'}
        
        # Simulate posting data to update the post
        response = self.client.post(url, data)

        # Check that the response is a redirect (status code 302)
        expected_status_code = 302
        actual_status_code = response.status_code
        print(f"Expected status code: {expected_status_code}, Actual status code: {actual_status_code}")
        self.assertEqual(actual_status_code, expected_status_code)
        
        # Refresh the post instance from the database
        post.refresh_from_db()
        
        # Check that the post title has been updated
        expected_title = 'Updated Post'
        actual_title = post.title
        print(f"Expected title: {expected_title}, Actual title: {actual_title}")
        self.assertEqual(actual_title, expected_title)

    def test_delete_post(self):
        self.client.force_login(self.user)
        post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.profile)
        url = reverse('blogApp:delete_post', kwargs={'post_id': post.id})
        
        # Simulate posting data to delete the post
        response = self.client.post(url)
        
        # Check that the response is a redirect (status code 302)
        expected_status_code = 302
        actual_status_code = response.status_code
        print(f"Expected status code: {expected_status_code}, Actual status code: {actual_status_code}")
        self.assertEqual(actual_status_code, expected_status_code)
        
        # Check that no posts exist after deletion
        expected_post_count = 0
        actual_post_count = Post.objects.count()
        print(f"Expected post count: {expected_post_count}, Actual post count: {actual_post_count}")
        self.assertEqual(actual_post_count, expected_post_count)
