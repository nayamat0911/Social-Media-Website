from django.urls import path
from .import views

app_name='app_login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login_page'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_page, name='logout_page'),
    path('profile/', views.User_Profile, name='User_Profile'),
    path('search_Profile/<username>/', views.User__view, name='User__view'),
    path('follow/<username>/', views.follow, name='follow'),
    path('unfollow/<username>/', views.unfollow, name='unfollow'),
]
