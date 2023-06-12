from django.shortcuts import render, redirect
from django.contrib.auth.models import User 

# Create your views here.

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

def login(request):
    return render(request, 'auth_app/login.html', {})
