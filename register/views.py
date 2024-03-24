from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        r_form = RegisterForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            username = r_form.cleaned_data.get('username')
            messages.success(request, f'Welcome to Portfol.io, {username}!')
            return redirect('login')
        else:
            messages.warning(request, f"Sorry, something about that wasn't right. Please try again.")
    else:
        r_form = RegisterForm()
    return render(request, 'register/register.html', {'r_form': r_form})


@login_required
def profile(request):
    return render(request, 'register/profile.html')


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'register/logout.html', {})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            messages.warning(request, f"Sorry, something about that wasn't right. Please try again.")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form,
               'p_form': p_form}

    return render(request, 'register/edit_profile.html', context)