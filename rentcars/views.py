from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import BookingForm
from .models import Car, Booking
from .forms import EmployeeRegisterForm




# Home page with login options
def home(request):
    return render(request, "rentcars/home.html")

# Redirect to Django admin panel
def redirect_to_admin(request):
    return redirect('/admin/')

# User registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    
    return render(request, "rentcars/register.html", {"form": form})

# User login view
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")  # Redirect to user dashboard
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "rentcars/login.html")

# User logout view
def user_logout(request):
    logout(request)
    return redirect("home")

# List all available cars
def car_list(request):
    cars = Car.objects.filter(available=True)
    return render(request, "rentcars/car_list.html", {"cars": cars})

# View details of a specific car
def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, "rentcars/car_detail.html", {"car": car})

# Book a car (only for logged-in users)
@login_required
def book_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.car = car
            booking.customer_name = request.user.username  # Set username as customer name
            booking.customer_email = request.user.email  # Set email from user account
            booking.save()
            return redirect("dashboard")  # Redirect to user dashboard after booking
    else:
        form = BookingForm()

    return render(request, "rentcars/booking_form.html", {"form": form, "car": car})

# User dashboard to view their bookings
@login_required
def dashboard(request):
    bookings = Booking.objects.filter(customer_name=request.user.username)  # Get only user's bookings
    return render(request, "rentcars/dashboard.html", {"bookings": bookings})

# Admin view for all bookings
@login_required
def admin_bookings(request):
    if not request.user.is_superuser:
        return redirect("home")  # Restrict access to admin only
    
    bookings = Booking.objects.all()
    return render(request, "rentcars/admin_bookings.html", {"bookings": bookings})


def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('employee_dashboard')  # Redirect to employee dashboard
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = EmployeeRegisterForm()
    
    return render(request, 'accounts/employee_register.html', {'form': form})
