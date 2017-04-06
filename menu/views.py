from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Items, Meal
from os.path import dirname, abspath
import populate
from datetime import date


def index(request):
    # check if request is post and handle appropriately by storing file in media
    if request.method == 'POST' and request.FILES['myfile']:
        # recieve and store file in /media folder
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # call population script to use add uploaded file data to database
        populate.populate(dirname(dirname(abspath(__file__))) + uploaded_file_url)
        return render(request, 'menu.html', {
            'uploaded_file_url': uploaded_file_url
        })

    # if database has no data then cathc error and display menu.html page
    # if user is authorized shows upload option else shoes blank page
    try:
        # display today's menu to visitors if request is not a post request
        current_date = '2017-02-14'  # explicitly setting date for debugging in 'yyyy-mm-dd' format
        # current_date = date.today().isoformat()
        meal_types = Meal.objects.filter(date=current_date)
        day = meal_types[0].day
        food = [Items.objects.filter(meal=i) for i in meal_types]
    except:
        return  render(request, 'menu.html')
    return render(request, 'menu.html', {'types': meal_types, 'items': food, 'date': current_date, 'day': day})
