from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # ✅ Use CustomUser instead of User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # ✅ Use CustomUser for normal users too
        fields = ['username', 'email', 'password1', 'password2']

class EmployeeRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # ✅ Already correct
        fields = ['username', 'email', 'password1', 'password2']
