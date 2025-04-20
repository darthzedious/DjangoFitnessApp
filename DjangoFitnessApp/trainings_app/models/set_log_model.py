from django.db import models

from .training_exercise_model import TrainingExercise


class SetLog(models.Model):
    training_exercise = models.ForeignKey(
        to=TrainingExercise,
        on_delete=models.CASCADE,
        related_name="sets",
    )

    set_number = models.PositiveIntegerField()

    reps_number = models.PositiveIntegerField()

    weight = models.FloatField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.training_exercise.name}: set: {self.set_number}, reps: {self.reps_number}, weight: {self.weight}."
