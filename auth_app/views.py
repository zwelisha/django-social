from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 

@login_required
def home(request):
    return render(request, 'auth_app/index.html', {})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('userName')
        first_name = request.POST.get('userFirstName')
        last_name = request.POST.get('userLastName')
        email = request.POST.get('userEmail')
        password = request.POST.get('userPassword')

        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect('login-page')

    return render(request, 'auth_app/register.html', {})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['userPassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse("User not found!")
    return render(request, 'auth_app/login.html', {})

def user_logout(request):
    logout(request)
    return redirect('login-page')