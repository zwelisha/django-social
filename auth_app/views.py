from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'auth_app/index.html', {})

def register(request):
    return render(request, 'auth_app/register.html', {})

def login(request):
    pass
