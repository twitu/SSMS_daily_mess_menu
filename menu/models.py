from __future__ import unicode_literals

from django.db import models

class Meal(models.Model):
    date = models.DateField(null=False, blank=False)
    meal_type = models.CharField(max_length=30, choices=(('grub','GRUB'),('lunch', 'LUNCH') , ('dinner','DINNER'), ('breakfast','BREAKFAST')))
    day = models.CharField(max_length=10, null=True)
    def __unicode__(self):
        return str(self.date) + str(self.meal_type)
class Items(models.Model):
    item = models.CharField(null=False, blank=False, max_length=30)
    meal = models.ForeignKey('Meal')
    def __unicode__(self):
        return str(self.item) + str(self.meal.date)