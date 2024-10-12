from django.shortcuts import render
from django.http import JsonResponse
from .models import CalendarEvent

def calendar_view(request):
    # Example of retrieving an event or creating one if none exists
    event = CalendarEvent.objects.first()
    if not event:
        event = CalendarEvent.objects.create(date="2024-01-01")
    data = {
        "year": event.date.year,
        "month": event.date.month,
        "day": event.date.day,
    }
    return JsonResponse(data)
from django.shortcuts import render

# Create your views here.
