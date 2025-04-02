from django.db import models

from DjangoFitnessApp.meals_app.models import DailyMeal


class DailyConsumptionManager(models.Manager):

    def update_totals(self, daily_consumption):
        """Recalculate total macros consumed for the day based on related DailyMeal entries."""

        meals = DailyMeal.objects.filter(profile=daily_consumption.profile, date=daily_consumption.date)

        daily_consumption.total_calories = sum(meal.calories for meal in meals)
        daily_consumption.total_protein = sum(meal.protein for meal in meals)

        daily_consumption.total_carbs = sum(meal.carbs for meal in meals)
        daily_consumption.total_sugars = sum(meal.sugars for meal in meals if meal.sugars is not None)

        daily_consumption.total_fats = sum(meal.fats for meal in meals)


        daily_consumption.total_fiber = sum(meal.fiber for meal in meals if meal.fiber is not None)
        daily_consumption.total_sodium = sum(meal.sodium for meal in meals if meal.sodium is not None)

        daily_consumption.save()
