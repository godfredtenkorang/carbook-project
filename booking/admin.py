from django.contrib import admin
from .models import Booking, FeaturedBooking

admin.site.register(Booking)
admin.site.register(FeaturedBooking)