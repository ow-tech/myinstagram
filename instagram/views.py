from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required




def main(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'instagram/main.html', context)

@login_required(login_url='/accounts/login')
def single_post(request):

    context ={

    }
    return render(request, 'instagram/single_post.html', context)