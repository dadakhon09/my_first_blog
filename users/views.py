from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            user.save()
            Profile.objects.create(user=user)
            messages.success(request, f'Your account {username} has been created! Now you may log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def profile_list(request):
    pl = get_user_model().objects.all()
    return render(request, 'profile_list.html', {'users':pl})


@login_required
def profile(request, pk):
    is_logged=False
    a = request.user
    all_users = Profile.objects.get(pk=pk)
    author = Profile.objects.get(user=a)
    if all_users.pk == author.pk:
        is_logged = True
    else:
        is_logged = False
    return render(request, 'profile.html', {'author': author, 'all_users':all_users, 'is_logged':is_logged})


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile', kwargs={slug:slug})
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'update_profile.html', context)
