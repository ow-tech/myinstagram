from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, ProfileUpdateForm



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
        form = NewPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save() 
            return redirect('single_image') 
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
def profile(request):
    if request.method =='POST':
        # user_update_form = UserUpdateForm(request.POST,instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES)

        if profile_update_form.is_valid:
            # user_update_form.is_valid()
            # user_update_form.save()
            profile_update_form.save()
            return redirect('profile')
    else:
        # user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm()

    context = {
        # 'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    return render(request, 'users/profile.html', context)

