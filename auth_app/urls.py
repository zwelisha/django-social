from django.urls import path
from .views import home, register, user_login, user_logout, posts

urlpatterns = [
    path("", home, name="home-page"),
    path("home/", home, name="home-page"),
    #path("timeline/", timeline, name="timeline-page"),
    path("posts/", posts, name="posts-page"),
    path("register/", register, name="register-page"),
    path("login/", user_login, name="login-page"),
    path("logout/", user_logout, name="logout"),
]
