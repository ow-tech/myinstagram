from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,  ProfileUpdateForm
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {"form":form})
def profile(request):
    # profiles = get_object_or_404(Profile, pk=profile_user)
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
        'profile_update_form': profile_update_form,
        # 'profiles':profiles
    }
    return render(request, 'instagram/profile.html', context)

