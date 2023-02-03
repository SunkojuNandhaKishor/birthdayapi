from django.urls import path
from .views import get_requests_count, calculate_age,view

urlpatterns = [
    path('get_requests_count/', get_requests_count, name='get_requests_count'),
    path('calculate_age/', calculate_age, name='calculate_age'),
    path('',view)
]