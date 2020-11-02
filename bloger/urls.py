from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home, name='blog'),
    path('<int:id>', views.like_testing, name='like'),
    path('like/<int:id>', views.CCounting, name='likes'),
    path('<str:slug>', views.Self_Blog, name='blog'),
]




