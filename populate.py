import os, django, csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailymenu.settings')
django.setup()

from menu.models import Meal, Items

row = csv.reader(open(r'mess_menu.csv', 'r'))

def populate():
    columns = list(zip(*row))
    for i in columns:
        date, day = i[0], i[1]
        breakfast = Meal(day=day,date=date, meal_type='BREAKFAST')
        lunch = Meal(day=day,date=date, meal_type=i[11])
        dinner = Meal(day=day,date=date, meal_type=i[23])
        breakfast.save()
        lunch.save()
        dinner.save()
        for j in range(2, 11):
            if i[j]: Items.objects.get_or_create(item=i[j], meal=breakfast)
        for j in range(12, 23):
            if i[j]: Items.objects.get_or_create(item=i[j], meal=lunch)
        for j in range(24, 34):
            if i[j]: Items.objects.get_or_create(item=i[j], meal=dinner)
if __name__=='__main__':
    populate()
