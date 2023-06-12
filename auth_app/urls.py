from django.urls import path
from .views import home, register, user_login, user_logout
urlpatterns = [
   path('home/', home, name="home-page"),
   path('register/', register, name="register-page"),
   path('login/', user_login, name="login-page"),
   path('logout/', user_logout, name="logout")
]