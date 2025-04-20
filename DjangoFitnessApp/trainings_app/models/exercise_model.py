from django.db import models

from DjangoFitnessApp.trainings_app.choices import ExerciseTypeChoices


class Exercise(models.Model):

    name = models.CharField(
        max_length=100,
    )

    equipment_brand = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    exercise_type = models.CharField(
        choices=ExerciseTypeChoices.choices,
    )

    exercise_picture = models.ImageField(
        upload_to="exercise_picture/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
