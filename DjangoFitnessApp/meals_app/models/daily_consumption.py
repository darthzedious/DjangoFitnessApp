from django.db import models

from DjangoFitnessApp.accounts.models import Profile
from DjangoFitnessApp.meals_app.managers import DailyConsumptionManager


class DailyConsumption(models.Model):
    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="daily_consumptions",
    )

    date = models.DateField(
        auto_now_add=True,
    )

    total_calories = models.FloatField(
        default=0.0,
    )

    total_protein = models.FloatField(
        default=0.0,
    )

    total_carbs = models.FloatField(
        default=0.0,
    )

    total_sugars = models.FloatField(
        default=0.0,
        null=True,
        blank=True,
    )

    total_fats = models.FloatField(
        default=0.0,
    )

    total_fiber = models.FloatField(
        default=0.0,
        null=True,
        blank=True,
    )

    total_sodium = models.FloatField(
        default=0.0,
        null=True,
        blank=True,
    )

    objects = DailyConsumptionManager()

    def __str__(self):
        return f"{self.profile.get_full_name()} - {self.date}"
