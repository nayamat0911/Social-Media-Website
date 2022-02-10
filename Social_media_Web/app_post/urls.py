from django.urls import path
from .import views

app_name='app_post'

urlpatterns = [
    path('', views.Home,name='Home'),
    path('likeed/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/', views.Unliked,name='Unliked'),
]
