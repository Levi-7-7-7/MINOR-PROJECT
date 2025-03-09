from django.contrib import admin
from django.utils.html import format_html
from .models import Car, Booking, CarImage

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "price_per_day", "available", "car_thumbnail")
    
    def car_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    car_thumbnail.short_description = "Image"

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ("car", "image")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "car", "start_date", "end_date")
