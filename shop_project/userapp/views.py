from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(data['email'], data['full_name'], data['phone_number'], data['password'])
            login(request, user)
            messages.success(request, 'you registered successfully', 'success')
            return redirect('shop:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


