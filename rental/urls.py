from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
    path('about-us/', views.about, name='about'),
    path('services/', views.service, name='services'),
    path('contact-us/', views.contact, name='contact'),
    path('T&Cs/', views.terms_and_conditions, name='terms-and-conditions'),
    path('logout/', views.logout_view),
]