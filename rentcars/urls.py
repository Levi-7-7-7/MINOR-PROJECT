from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page with login options
    path('car_list/', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('car/<int:car_id>/book/', views.book_car, name='book_car'),

    # User authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='rentcars/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # Dashboard and admin views
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard
    path('admin_bookings/', views.admin_bookings, name='admin_bookings'),  # Admin bookings view

    # Django admin panel redirect
    path('admin/', views.redirect_to_admin, name='admin_login'),
]
