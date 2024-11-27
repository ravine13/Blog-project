from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
