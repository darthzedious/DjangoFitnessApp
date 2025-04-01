from django.core.validators import MinValueValidator
from django.db import models

from DjangoFitnessApp.accounts.models import Profile
from DjangoFitnessApp.meals_app.choices import MealType
from DjangoFitnessApp.meals_app.models import Meal


class DailyMeal(models.Model):
    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="daily_meals",
    )

    meal = models.ForeignKey(
        to=Meal,
        on_delete=models.CASCADE,
        related_name="daily_meals",
    )

    date = models.DateField(
        auto_now_add=True
    )

    meal_type = models.CharField(
        max_length=10,
        choices=MealType.choices,
    )

    grams = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ]
    )

    calories = models.FloatField()

    protein = models.FloatField()

    carbs = models.FloatField()

    sugars = models.FloatField(
        null=True,
        blank=True,
    )

    fats = models.FloatField()

    saturated_fats = models.FloatField(
        null=True,
        blank=True,
    )

    fiber = models.FloatField(
        blank=True,
        null=True,
    )

    sodium = models.FloatField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.profile.get_full_name()} - {self.meal.name} ({self.meal_type}) on {self.date}"
