from django.db import models

from DjangoFitnessApp.meals_app.models import DailyMeal


class DailyConsumptionManager(models.Manager):

    def update_totals(self, daily_consumption):
        """Recalculate total macros consumed for the day based on related DailyMeal entries."""

        meals = DailyMeal.objects.filter(profile=daily_consumption.profile, date=daily_consumption.date)

        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_sugars = 0
        total_fats = 0
        total_fiber = 0
        total_sodium = 0

        for meal in meals:
            total_calories += meal.calories or 0
            total_protein += meal.protein or 0
            total_carbs += meal.carbs or 0
            total_sugars += meal.sugars or 0
            total_fats += meal.fats or 0
            total_fiber += meal.fiber or 0
            total_sodium += meal.sodium or 0

        daily_consumption.total_calories = total_calories
        daily_consumption.total_protein = total_protein
        daily_consumption.total_carbs = total_carbs
        daily_consumption.total_sugars = total_sugars
        daily_consumption.total_fats = total_fats
        daily_consumption.total_fiber = total_fiber
        daily_consumption.total_sodium = total_sodium

        daily_consumption.save()
