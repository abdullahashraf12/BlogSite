from django.test import TestCase
from userauths.models import User
from ..models import Post, Comment, Category, Tag, Profile

class ModelsTestCase(TestCase):

    def setUp(self):
        # Create a user with email as username
        self.user = User.objects.create_user(
            username='memo2@gmail.com',
            password='password123',
            email='memo2@gmail.com'
        )
        # Create a profile for the user with a profile picture
        self.profile = Profile.objects.create(
            user=self.user,
            bio='This is a test bio.',
            profile_picture='mypic.jpg'  # Use the image in the same directory
        )
        # Create a category and tag for testing
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.tag = Tag.objects.create(name='Test Tag', slug='test-tag')

    def test_create_post(self):
        # Create a post and associate it with the user profile
        post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.profile,
        )
        post.categories.add(self.category)
        post.tags.add(self.tag)

        # Verify the post's attributes
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post content.')
        self.assertEqual(post.author.user.username, 'memo2@gmail.com')
        self.assertEqual(post.categories.count(), 1)
        self.assertEqual(post.tags.count(), 1)

    def test_create_comment(self):
        # Create a post for the comment
        post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.profile,
        )
        # Create a comment and associate it with the post and user profile
        comment = Comment.objects.create(
            post=post,
            author=self.profile,
            content='This is a test comment.',
        )

        # Verify the comment's attributes
        self.assertEqual(comment.post.title, 'Test Post')
        self.assertEqual(comment.author.user.username, 'memo2@gmail.com')
        self.assertEqual(comment.content, 'This is a test comment.')

    def test_create_profile(self):
        # Verify the profile's attributes
        self.assertEqual(self.profile.user.username, 'memo2@gmail.com')
        self.assertEqual(self.profile.bio, 'This is a test bio.')
        self.assertEqual(self.profile.profile_picture, 'mypic.jpg')
