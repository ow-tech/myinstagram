from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to="images/", null=False, default='SOME STRING')
    image_name = models.CharField(max_length=100)
    caption = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  '{} {}'.format(self.author, self.caption) 

    def save_post(self):
        self.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()


    def __str__(self):
        return '{} {}'.format(self.user, self.bio)


    def save_profile(self):
        self.save()