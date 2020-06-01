from django import forms
from .models import Image
from django.contrib.auth.models import User


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['author','date_posted','likes','comments']


# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username']

