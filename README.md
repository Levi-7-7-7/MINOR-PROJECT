# Rental Cars - Minor Project

## Project Overview
Rental Cars is a web-based car rental system that allows users to book cars, manage their bookings, and provides employees with tools to approve or reject rental requests.

## Features
- User Registration & Login
- Employee Registration & Login
- Admin Panel for managing users and bookings
- Browse available cars
- Book a car for a specific period
- Employee dashboard to approve/reject bookings
- Track booking history
- Mark bookings as completed

## Technologies Used
- Django (Python)
- SQLite (Database)
- Bootstrap (Frontend)
- HTML, CSS, JavaScript

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/yourusername/rental-cars.git  
cd rental-cars  

### 2. Create a Virtual Environment
Linux/macOS:  
python -m venv venv  
source venv/bin/activate  

Windows:  
python -m venv venv  
venv\Scripts\activate  

### 3. Install Dependencies
pip install -r requirements.txt  

### 4. Apply Migrations
python manage.py makemigrations  
python manage.py migrate  

### 5. Create Superuser (Admin)
python manage.py createsuperuser  

### 6. Run the Development Server
python manage.py runserver  

Visit **http://127.0.0.1:8000/** in your browser.

## User Roles

### Admin
- Full access to the Django Admin Panel
- Manage users, employees, cars, and bookings

### Employee
- Can log in to the Employee Dashboard
- View and manage user bookings
- Approve or reject booking requests
- Mark bookings as completed

### Customer
- Can register and log in
- Browse available cars
- Book a car for a specific period
- View booking history

## URL Endpoints

### User Routes
/accounts/register/ - Register a new user  
/accounts/login/ - User login  
/accounts/dashboard/ - View user bookings  
/accounts/logout/ - Logout  

### Employee Routes
/accounts/employee/register/ - Register an employee  
/accounts/employee/login/ - Employee login  
/accounts/employee/dashboard/ - Manage user bookings  
/accounts/employee/approve-booking/<booking_id>/ - Approve a booking  
/accounts/employee/reject-booking/<booking_id>/ - Reject a booking  
/accounts/employee/undo-approval/<booking_id>/ - Undo approval  
/accounts/employee/complete-booking/<booking_id>/ - Mark booking as completed  
/accounts/employee/reapprove-booking/<booking_id>/ - Reapprove a rejected booking  

### Admin Panel
/admin/ - Access the Django Admin Panel  

## Notes
- Default database: SQLite (`db.sqlite3`)
- Employees must be registered separately by an admin
- Superusers have full control over the system

## Contribution
Fork the repository and submit a pull request with your changes.

## License
This project is open-source and available under the MIT License.

---
Rental Cars - Minor Project  
Developed by **Lijo P Thomas**  
