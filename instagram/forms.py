from django import forms
from .models import Profile, Post
from django.contrib.auth.models import User


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author','date_posted']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

