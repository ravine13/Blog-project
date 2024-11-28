from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),                # Root URL for the home page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard URL
    path('logout/', views.user_logout, name='logout'),       # Logout URL
    path('profile/', views.profile, name='profile'),         # Profile page
    path('posts/', views.post_list, name='post_list'),       # List of posts
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Post detail
    path('register/', views.register, name='register'),      # Registration page
    path('login/', views.login_view, name='login'),          # Login page
]
