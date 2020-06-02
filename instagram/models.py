from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to="images/", null=False, default='SOME STRING')
    image_name = models.CharField(max_length=100)
    caption = models.TextField()
    # likes = models.ManyToManyField(User, default = None, blank=True)
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

    @property
    def num_likes(self):
        return self.likes.all().count()

class Comments(models.Model):
    image = models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{}'.format(self.content)

    def vaild(self):
        self.vaild = True
        self.save()



# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     post = models.ForeignKey(Image, on_delete=models.CASCADE)
#     value = models.CharField(choices=, default='Like', max_length=10)






