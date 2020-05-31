from django.test import TestCase
from .models import Image

# Create your tests here.

class PostTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.alex=Image(caption="We are who we are.")

    #Testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.alex,Image))

    #Testing Save method
    def test_save_method(self):
        self.alex.save_image()
        image= Image.objects.all()
        self.assertTrue(len(image) > 0)


class ProfileTestCase(TestCase):
    def setUp(self):
        self.alex=Profile(bio = 'Each day Is Trying and Trying')

    def test_instance(self):
        self.assertTrue(isinstance(self.alex,Profile))
    
    def test_save_method(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)