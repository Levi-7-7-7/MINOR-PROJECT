from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')

    # Fix conflicts with Django’s default User model fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Ensure unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Ensure unique related_name
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
