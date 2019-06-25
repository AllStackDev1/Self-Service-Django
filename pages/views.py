from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# from django.http import HttpResponse


def signup(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            # Check email
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User already registered!')
                return redirect('signup')
            else:
                # Looks good
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
                auth.login(request, user)
                messages.success(request, 'Welcome ' + first_name)
                return redirect('dashboard')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')
    else:
        return render(request, 'pages/auth/signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome ' + user.first_name)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'pages/auth/login.html')


def logout(request):
    return redirect('login')


menus = [
    {
        'id': 1,
        'image': 'img/daily-time-sheet.jpg',
        'link': 'daily-time-sheet',
        'title': 'Daily Time Sheet',
    },
    {
        'id': 2,
        'image': 'img/daily-time-sheet.jpg',
        'link': 'daily-time-sheet',
        'title': 'BTL Plus',
    },
    {
        'id': 3,
        'image': 'img/vehicle-request.png',
        'link': 'vehicle-request-form',
        'title': 'Vehicle Request Form',
    },
    {
        'id': 4,
        'image': 'img/it-service.png',
        'link': 'it-service',
        'title': 'IT Service',
    },
{
        'id': 5,
        'image': 'img/leave-request.png',
        'link': 'leave-request',
        'title': 'Leave Request',
    },
    {
        'id': 6,
        'image': 'img/feedback.png',
        'link': 'event-feedback',
        'title': 'Event Feedback',
    },
]


def dashboard(request):
    return render(request, 'pages/dashboard.html', {'menus': menus})

