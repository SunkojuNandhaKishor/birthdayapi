from django.shortcuts import render
from django.http import JsonResponse
from .models import AgeRequest
import datetime 
from dateutil import relativedelta

def get_requests_count(request):
    count = AgeRequest.objects.count()
    return JsonResponse({'count': count})

def calculate_age(request):
    dob = request.GET.get('dob')
    start_date = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
    end_date = datetime.date.today()
    print(start_date,end_date,type(start_date),type(end_date))
    delta = relativedelta.relativedelta(end_date, start_date)
    AgeRequest.objects.create(dob=dob)
    return JsonResponse({'age': str(delta.years) + '\tYears <br>'+ str(delta.months) + '\tmonths <br>'+ str(delta.days) + '\tdays <br>'})

def view(request):
    return render(request, 'calculate_age.html')