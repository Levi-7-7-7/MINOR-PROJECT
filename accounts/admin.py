from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

CustomUser = get_user_model()  # ✅ Get the custom user model

# ✅ Check if CustomUser is registered before unregistering
if admin.site.is_registered(CustomUser):
    admin.site.unregister(CustomUser)

# Custom filter for employees (staff but not superusers)
class EmployeeFilter(admin.SimpleListFilter):
    title = 'Employee Status'
    parameter_name = 'employee'

    def lookups(self, request, model_admin):
        return [('yes', 'Employees')]

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(is_staff=True, is_superuser=False)
        return queryset

# Custom User Admin to display all users properly
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_staff", "is_superuser", "date_joined")
    list_filter = (EmployeeFilter, "is_staff", "is_superuser", "role")
    search_fields = ("username", "email")

# ✅ Register the custom user model in the admin panel
admin.site.register(CustomUser, CustomUserAdmin)
