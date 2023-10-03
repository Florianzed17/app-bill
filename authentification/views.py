from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('events:home')
        else:
            messages.error(request, 'Identifiants invalides. Veuillez réessayer.')

    return render(request, 'auth/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté !")
    return redirect('events:home')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            password = form.cleaned_data['password1']
            user = authenticate(username=user.username, password=password)
            login(request, user)
            messages.success(request, "Inscription réussie !")
            return redirect('events:home')
    else:
        form = RegisterUserForm()

    return render(request, 'auth/register_user.html', {'form': form})
