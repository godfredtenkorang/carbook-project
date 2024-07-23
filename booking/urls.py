from django.urls import path
from . import views

urlpatterns = [
    path('<slug:vehicle_slug>/', views.book_vehicle, name='vehicle-book'),
    path('featured/<slug:featured_slug>/', views.books_vehicle, name='vehicle-books'),
]