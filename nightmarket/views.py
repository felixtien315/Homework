from django.shortcuts import render
from .models import Food

def food_list(request):
    foods = Food.objects.all().select_related('vendor__night_market')
    return render(request, 'nightmarket/food_list.html', {'foods': foods})