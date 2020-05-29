from django.shortcuts import render
from django.http import HttpResponse
from .models import Post




def main(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'instagram/main.html', context)
