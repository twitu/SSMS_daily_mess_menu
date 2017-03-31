from django.shortcuts import render

from django.http import HttpResponse
from .models import Items, Meal
from datetime import date

def index(request):
    # current_date in 'yyyy-mm-dd' format
    current_date = '2017-02-14'  # explicitly setting date for debugging
    #current_date = date.today().isoformat()
    meal_types = Meal.objects.filter(date=current_date)
    day = meal_types[0].day
    food = [Items.objects.filter(meal=i) for i in meal_types]
    return render(request, 'menu.html', {'types':meal_types, 'items':food, 'date':current_date, 'day':day})
