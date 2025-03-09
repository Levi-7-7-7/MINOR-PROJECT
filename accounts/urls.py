# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # User URLs
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Employee URLs
    path('employee/register/', views.register_employee, name='register_employee'),
    path('employee/login/', views.employee_login, name='employee_login'),
    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),

    # Booking Management URLs
    path('employee/approve-booking/<int:booking_id>/', views.approve_booking, name='approve_booking'),
    path('employee/reject-booking/<int:booking_id>/', views.reject_booking, name='reject_booking'),
    path('employee/undo_approval/<int:booking_id>/', views.undo_approval, name='undo_approval'),
    path('employee/complete_booking/<int:booking_id>/', views.complete_booking, name='complete_booking'),
    
    # ✅ Fix: Add reapprove_booking
    path('employee/reapprove-booking/<int:booking_id>/', views.reapprove_booking, name='reapprove_booking'),
    # accounts/urls.py
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
 
]
