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
        return  '{}'.format(self.image_name)

    def save_post(self):
        self.save()
    @classmethod
    def delete_post(cls, id):
        image = cls.objects.filter(id).all()
        image.delete() 


    @classmethod
    def get_single_image_by_id(cls, id):
        image = cls.objects.filter(id).all()
        return image

    @classmethod
    def search_by_author(cls, search_term):
        users = cls.objects.filter(author__username__icontains=search_term)
        return users

    






