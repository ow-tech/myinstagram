from django.test import TestCase
from .models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        self.alex=Profile(bio = 'Each day Is Trying and Trying')

    def test_instance(self):
        self.assertTrue(isinstance(self.alex,Profile))
    
    def test_save_method(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)