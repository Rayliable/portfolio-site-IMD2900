from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome to Portfol.io, {username}!')
            return redirect('login')
        else:
            messages.warning(request, f"Sorry, something about that wasn't right. Please try again.")
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'register/profile.html')


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'register/logout.html', {})
