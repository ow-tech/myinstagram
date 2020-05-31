from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, ProfileUpdateForm



@login_required(login_url='')
def main(request):
    context = {
        'posts': Image.objects.all()
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

@login_required(login_url='/accounts/login')
def single_post(request):

    context ={

    }
    return render(request, 'instagram/single_post.html', context)

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