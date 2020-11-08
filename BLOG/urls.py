from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.Home, name='home'),
    path('delate/<int:id>', views.deleting, name='delate'),
    path('logout', LogoutView.as_view, name='logout'),
    path('edite/<int:id>', views.edite, name='edite'),
    path('category/<int:id>', views.get_category, name='category'),
    path('<str:slug>', views.details, name='details'),
]




