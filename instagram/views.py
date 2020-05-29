from django.shortcuts import render
from django.http import HttpResponse
from .models import Post




def main(request):
    context = {
        'Posts': Post
    }
    return render(request, 'instagram/main.html', context)
