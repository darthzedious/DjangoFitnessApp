from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .exercise_model import Exercise
from .training_session_model import TrainingSession


class TrainingExercise(models.Model):
    training_session = models.ForeignKey(
        to=TrainingSession,
        on_delete=models.CASCADE,
        related_name="training_exercise",
    )

    exercise = models.ForeignKey(
        to=Exercise,
        on_delete=models.CASCADE,
        related_name="training_exercise",
    )

    rest_seconds = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    effort_level = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        null=True,
        blank=True,
        help_text="RPE (Rate of Perceived Exertion) from 1 to 10",
    )

    notes = models.TextField(
        null=True,
        blank=True,
    )
