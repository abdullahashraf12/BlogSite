from django.test import TestCase
from ..models import User, Profile

class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='memo3@gmail.com'
        )
        self.profile = Profile.objects.create(user=self.user, bio='')

    def test_user_registration(self):
        self.assertEqual(User.objects.count(), 1)

    def test_user_login(self):
        response = self.client.login(username='memo3@gmail.com', password='password123')
        self.assertTrue(response)

    def test_profile_management(self):
        self.client.force_login(self.user)
        self.user.profile.bio = 'Updated bio'
        self.user.profile.save()
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.bio, 'Updated bio')
