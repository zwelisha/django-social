from django.urls import path
from .views import home, register, login
urlpatterns = [
   path('home/', home, name="home-page"),
   path('register/', register, name="register-page"),
   path('login/', login, name="login-page")
]