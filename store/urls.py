from django.urls import path
from django.contrib.auth import views as auth_views
from store import views

urlpatterns = [
    # Главная панель
    path('', views.dashboard, name='dashboard'),
    
    # Товары
    path('product/add/', views.add_product, name='add_product'),
    path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    
    # Вход и регистрация
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
]