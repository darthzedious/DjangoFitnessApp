from django.core.validators import MinValueValidator
from django.db import models

from DjangoFitnessApp.accounts.models import Profile
from DjangoFitnessApp.goal_app.calculations import calculate_bmr, calculate_amr, calculate_goal_calories, \
    calculate_daily_macros
from DjangoFitnessApp.goal_app.choices import ActivityChoices, GoalChoices


class Goal(models.Model):
    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="goal",
    )

    weight = models.FloatField(
        validators=[MinValueValidator(1)],
    )

    height = models.FloatField(
        validators=[MinValueValidator(1)],
    )

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
    )

    gender = models.CharField(
        max_length=10,
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
        ],
    )

    activity = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        choices=ActivityChoices.choices,
    )


    goal_weight = models.FloatField(
        validators=[MinValueValidator(2)],
    )

    goal_type = models.CharField(
        max_length=20,
        choices=GoalChoices.choices,
        default="Maintain",
    )

    daily_calories = models.IntegerField(
        null=True,
        blank=True,
    )

    daily_protein = models.IntegerField(
        null=True,
        blank=True,
    )

    daily_carbohydrates = models.IntegerField(
        null=True,
        blank=True,
    )

    daily_fats = models.IntegerField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):
        bmr = calculate_bmr(self.gender, self.weight, self.height, self.age)
        amr = calculate_amr(bmr, self.activity)
        self.daily_calories = calculate_goal_calories(amr, self.goal_type)

        self.daily_carbohydrates, self.daily_protein, self.daily_fats = calculate_daily_macros(self.daily_calories, self.goal_type)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.profile.first_name} {self.profile.last_name} - {self.goal_type}"
