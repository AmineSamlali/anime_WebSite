from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('delate/<int:id>', views.deleting, name='delate'),
    path('edite/<int:id>', views.edite, name='edite'),
    path('category/<int:id>', views.get_category, name='category'),
    path('<str:slug>', views.details, name='details'),
]




