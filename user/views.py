from django.shortcuts import render
from django.http import JsonResponse
from .models import UserProfile

def user_view(request):
    user = UserProfile.objects.first()
    if not user:
        user = UserProfile.objects.create(
            first_name="John", last_name="Doe", date_of_birth="1990-01-01"
        )
    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "date_of_birth": user.date_of_birth,
        "age": user.age(),
    }
    return JsonResponse(data)
from django.shortcuts import render

# Create your views here.
