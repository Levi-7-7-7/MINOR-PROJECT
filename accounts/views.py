from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, EmployeeRegisterForm
from .models import CustomUser
from rentcars.models import Booking

# ✅ User Registration View
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('dashboard')  # Redirect to dashboard
        else:
            messages.error(request, "Registration failed: " + str(form.errors))
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# ✅ User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

# ✅ User Logout View
def user_logout(request):
    logout(request)
    return redirect('car_list')

# ✅ User Dashboard View (Only for logged-in users)
@login_required
def dashboard(request):
    bookings = Booking.objects.filter(customer_name=request.user.username)
    
    # Calculate rental amount
    for booking in bookings:
        rental_duration = (booking.end_date - booking.start_date).days
        booking.amount_to_be_paid = booking.car.price_per_day * rental_duration if rental_duration > 0 else 0

    return render(request, 'accounts/dashboard.html', {'bookings': bookings})

# ✅ Employee Registration View
def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'employee'  # Assign employee role
            user.is_staff = True  # Mark as staff
            user.save()
            messages.success(request, "Employee account created successfully!")
            return redirect('employee_login')
        else:
            messages.error(request, "Registration failed: " + str(form.errors))
    else:
        form = EmployeeRegisterForm()
    return render(request, 'accounts/register_employee.html', {'form': form})

# ✅ Employee Login View
def employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.role == 'employee':
            login(request, user)
            return redirect('employee_dashboard')
        else:
            messages.error(request, "Invalid credentials or not an employee account.")
    return render(request, 'accounts/employee_login.html')

# ✅ Employee Dashboard View (Only for employees)
@login_required
def employee_dashboard(request):
    if not request.user.is_staff:  # Ensure only employees can access this
        messages.error(request, "You do not have permission to view this page.")
        return redirect("home")

    bookings = Booking.objects.all().order_by('-start_date')  # Show recent bookings first
    return render(request, "accounts/employee_dashboard.html", {"bookings": bookings})

# ✅ Approve Booking
@login_required
def approve_booking(request, booking_id):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to perform this action.")
        return redirect("employee_dashboard")

    booking = get_object_or_404(Booking, id=booking_id)
    booking.approval_status = "approved"
    booking.save()
    messages.success(request, f"Booking for {booking.car.name} has been approved.")
    return redirect("employee_dashboard")

# ✅ Reject Booking
@login_required
def reject_booking(request, booking_id):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to perform this action.")
        return redirect("employee_dashboard")

    booking = get_object_or_404(Booking, id=booking_id)
    booking.approval_status = "rejected"
    booking.save()
    messages.warning(request, f"Booking for {booking.car.name} has been rejected.")
    return redirect("employee_dashboard")

# ✅ Undo Approval (Change status back to Pending)
@login_required
def undo_approval(request, booking_id):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to perform this action.")
        return redirect("employee_dashboard")

    booking = get_object_or_404(Booking, id=booking_id)
    booking.approval_status = "pending"
    booking.save()
    messages.info(request, f"Booking for {booking.car.name} is now pending again.")
    return redirect("employee_dashboard")

# ✅ Mark as Completed
@login_required
def complete_booking(request, booking_id):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to perform this action.")
        return redirect("employee_dashboard")

    booking = get_object_or_404(Booking, id=booking_id)
    booking.approval_status = "completed"
    booking.save()
    messages.success(request, f"Booking for {booking.car.name} is marked as completed.")
    return redirect("employee_dashboard")

# ✅ Reapprove a Rejected Booking
@login_required
def reapprove_booking(request, booking_id):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to perform this action.")
        return redirect("employee_dashboard")

    booking = get_object_or_404(Booking, id=booking_id)
    if booking.approval_status == "rejected":
        booking.approval_status = "approved"
        booking.save()
        messages.success(request, f"Booking for {booking.car.name} has been reapproved.")
    else:
        messages.warning(request, "Only rejected bookings can be reapproved.")

    return redirect("employee_dashboard")










# accounts/views.py

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer_name=request.user.username)

    # Only allow cancellation if the booking is still pending
    if booking.approval_status == "pending":
        booking.delete()
        messages.success(request, "Your booking has been canceled successfully.")
    else:
        messages.error(request, "You can only cancel pending bookings.")

    return redirect("dashboard")










