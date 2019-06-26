from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('daily-time-sheet/', views.daily_time_sheet, name='daily_time_sheet'),
    path('btl-plus/', views.btl_plus, name='btl_plus'),
    path('vehicle-request-form/', views.vehicle_request_form, name='vehicle_request_form'),
    path('it-service/', views.it_service, name='it_service'),
    path('leave-request/', views.leave_request, name='leave_request'),
    path('event-feedback/', views.event_feedback, name='event_feedback'),
]
