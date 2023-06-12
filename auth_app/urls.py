from django.urls import path
from .views import home, register
urlpatterns = [
   path('home/', home, name="home-page"),
   path('register/', register, name="register-page")
]