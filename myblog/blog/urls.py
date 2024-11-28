from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),        
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('logout/', views.user_logout, name='logout'),       
    path('profile/', views.profile, name='profile'),         
    path('posts/', views.post_list, name='post_list'),       
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  
    path('register/', views.register, name='register'),      
    path('login/', views.login_view, name='login'),    
    path('write/', views.write_story, name='write'),   
]
