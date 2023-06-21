from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name="home"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('order', views.order, name="orderpage"),
    path('search', views.search, name='search'),


]
