from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm



@login_required(login_url='')
def main(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'instagram/main.html', context)

@login_required(login_url='/auth/login')
def new_post(request):
    current_user = request.current_user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author =current_user
            post.save()
            return redirect("main_page")
    else:
        form = NewPostForm()
    return render(request,'new_post.html',{"form":form})

@login_required(login_url='/accounts/login')
def single_post(request):

    context ={

    }
    return render(request, 'instagram/single_post.html', context)