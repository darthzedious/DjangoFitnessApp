from django.db import models

from DjangoFitnessApp.accounts.models import Profile
from DjangoFitnessApp.trainings_app.choices import WorkoutTypeChoices


class TrainingSession(models.Model):
    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="training_session",
    )

    date = models.DateField()

    workout_type = models.CharField(
        max_length=30,
        choices=WorkoutTypeChoices.choices,
    )

    gym = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    training_duration_minutes = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.profile} - {self.date} - {self.workout_type}"
