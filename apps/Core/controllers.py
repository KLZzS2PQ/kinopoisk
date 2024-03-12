from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def singup(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        username = request.POST['username']
        email = request.POST['email']
        if password != repeat_password:
            return render(request, 'Core/auth/singup.html', {'error': 'Не совпадают пароли'})
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('singin')
    return render(request, 'Core/auth/singup.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('singin')
    return render(request, 'Core/auth/profile.html')


def singin(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'Core/auth/singin.html', {'error': 'Неверный логин или пароль'})
        login(request, user=user)
        return redirect('profile')
    return render(request, 'Core/auth/singin.html')


def singout(request):
    logout(request)
    return redirect('singin')



















