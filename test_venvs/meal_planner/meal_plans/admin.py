from django.contrib import admin

from meal_plans.models import Meal, foodChoices

admin.site.register(Meal)
admin.site.register(foodChoices)

