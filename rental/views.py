from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, CarForRent, Contact, FeaturedCarForRent, NeedADriver
from django.contrib import messages
from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    user = request.user
    if request.method == 'POST':
        pick_up_location = request.POST['pick_up_location']
        drop_off_location = request.POST['drop_off_location']
        pick_up_date = request.POST['pick_up_date']
        drop_off_date = request.POST['drop_off_date']
        pick_up_time= request.POST['pick_up_time']
        
        drivers = NeedADriver(user=user, pick_up_location=pick_up_location, drop_off_location=drop_off_location, pick_up_date=pick_up_date, drop_off_date=drop_off_date, pick_up_time=pick_up_time)
        drivers.save()
        
        send_mail(
            f"New Booking for a Driver Submission from {user.username}",
            f'Message:{pick_up_location} \n {drop_off_location} \n {pick_up_date} \n {drop_off_date}',
            user.email,  # From email
                [settings.EMAIL_HOST_USER],  # To email
                fail_silently=False,
        ),
        messages.success(request, 'Your form as been sent successfully! You will here from us soon...')
        return redirect('index')
    vehicles = FeaturedCarForRent.objects.all()
    context = {
        'vehicles': vehicles
    }
    return render(request, 'rental/index.html', context)

def about(request):
    return render(request, 'rental/about.html', {'title': 'About Us'})

def categories(request):
    
    all_categories = Category.objects.all()
    
    return {'all_categories': all_categories}

def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    vehicles = CarForRent.objects.filter(category=category)
    context = {
        'vehicles': vehicles,
        'category': category,
        'title': 'Vehicle'
    }
    return render(request, 'rental/list_category.html', context)


def service(request):
    return render(request, 'rental/services.html', {'title': 'Services'})

def contact(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contacts = Contact(fullname=fullname, email=email, subject=subject, message=message)
        contacts.save()
        messages.success(request, 'Your form has been sent successfully!')
        
        send_mail(
            f"New Form Submission from {fullname}",
            f'Message:{subject} \n {message} \n From {email}',
            email,  # From email
                [settings.EMAIL_HOST_USER],  # To email
                fail_silently=False,
        ),
        return redirect('contact')
    return render(request, 'rental/contact.html', {'title': 'Contact Us'})

def terms_and_conditions(request):
    return render(request, 'rental/terms_and_conditions.html', {'title': 'T&Cs'})

def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out successfully")
    return redirect('index')