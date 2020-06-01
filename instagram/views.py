from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Image
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm



@login_required(login_url='')
def main(request):
    context = {
        'posts': Image.objects.all().order_by('-date_posted')
    }
    return render(request, 'instagram/main.html', context)

@login_required(login_url='/auth/login')
def new_post(request):
    current_user = request.user
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

def update_post(request, pk):
    post = Image.objects.get(id=pk)
    form = NewPostForm(instance=post)

    if request.method == 'POST':
        form = NewPostForm(request.POST, instance=request.post)
        if form.is_valid():
            form.save() 
            return redirect('main_page') 
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'form':form,'post':post})

def delete_post(request, pk):
    post = Image.objects.get(id=pk)
    current_user = request.user

    if current_user == post.author and request.method == 'POST':
        post.delete()
        return redirect('main_page')
    context = {
        "post":post
    }
    return render(request, 'instagram/delete_post.html', context)


@login_required(login_url='/accounts/login')
def single_post(request, image_id):
    images = get_object_or_404(Image, pk=image_id)
    return render(request, 'instagram/single_post.html', {"images":images})

login_required(login_url='/accounts/login')

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_author(search_term)
        message = f"{ search_term }"
        return render(request, 'instagram/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'instagram/search.html',{"message":message})

