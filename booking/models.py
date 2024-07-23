from django.db import models
from rental.models import CarForRent, FeaturedCarForRent
from django.utils import timezone


class Booking(models.Model):
    vehicle = models.ForeignKey(CarForRent, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    pick_up_location = models.CharField(max_length=100)
    drop_off_location = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pick_up_date = models.CharField(max_length=20, null=True, blank=True)
    drop_off_date = models.CharField(max_length=20, null=True, blank=True)
    pick_up_time = models.CharField(max_length=20, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Bookings'
        ordering = ['-date_added',]
        
    def __str__(self):
        return self.vehicle.name
    
class FeaturedBooking(models.Model):
    vehicle = models.ForeignKey(FeaturedCarForRent, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    pick_up_location = models.CharField(max_length=100)
    drop_off_location = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pick_up_date = models.CharField(max_length=20, null=True, blank=True)
    drop_off_date = models.CharField(max_length=20, null=True, blank=True)
    pick_up_time = models.CharField(max_length=20, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Featured Bookings'
        ordering = ['-date_added',]
        
    def __str__(self):
        return self.vehicle.name