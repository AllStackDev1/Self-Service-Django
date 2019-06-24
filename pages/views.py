from django.shortcuts import render
# from django.http import HttpResponse


def login(request):
    return render(request, 'pages/auth/login.html')


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

