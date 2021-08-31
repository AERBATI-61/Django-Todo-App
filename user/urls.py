
from django.contrib import admin
from django.urls import path
from user import views
app_name = "user"
urlpatterns = [
    path('login', views.loginuser, name = "login"),
    path('logout', views.logoutuser, name = "logout"),
    path('register', views.registeruser, name = "register"),


]
