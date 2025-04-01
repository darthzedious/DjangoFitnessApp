from django.core.validators import MinValueValidator
from django.db import models

from DjangoFitnessApp.meals_app.choices import MealCategoryChoices


class Meal(models.Model):
    name = models.CharField(
        max_length=100,
    )

    brand = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    category = models.CharField(
        max_length=100,
        choices=MealCategoryChoices.choices,
        default=MealCategoryChoices.MY_MEALS,
    )

    # Values for the given portion
    calories_per_portion = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ],
    )

    grams_portion = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ],
    )

    protein_per_portion = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ],
    )

    carbs_per_portion = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ],
    )

    sugars_per_portion = models.FloatField(
        null=True,
        blank=True,
    )

    fats_per_portion = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ],
    )

    saturated_fats_per_portion = models.FloatField(
        null=True,
        blank=True,
    )

    fiber_per_portion = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0.0),
        ],
    )

    sodium_per_portion = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0.0),
        ],
    )

    # Auto-calculated values per-gram
    calories_per_gram = models.FloatField(
        blank=True,
        null=True,
    )

    protein_per_gram = models.FloatField(
        blank=True,
        null=True,
    )

    carbs_per_gram = models.FloatField(
        blank=True,
        null=True,
    )

    sugars_per_gram = models.FloatField(
        blank=True,
        null=True,
    )

    fats_per_gram = models.FloatField(
        blank=True,
        null=True,
    )

    saturated_fats_per_gram = models.FloatField(
        null=True,
        blank=True,
    )

    fiber_per_gram = models.FloatField(
        blank=True,
        null=True,
    )

    sodium_per_gram = models.FloatField(
        blank=True,
        null=True,
    )

    meal_picture = models.ImageField(
        upload_to="meal_pictures/",
        blank=True,
        null=True,
    )

    #
    # def save(self, *args, **kwargs):
    #     try:
    #         self.calories_per_gram = self.calories_per_portion / self.grams_portion
    #         self.protein_per_gram = self.protein_per_portion / self.grams_portion
    #         self.carbs_per_gram = self.carbs_per_portion / self.grams_portion
    #         self.fats_per_gram = self.fats_per_portion / self.grams_portion
    #         self.fiber_per_gram = (self.fiber_per_portion / self.grams_portion) if self.fiber_per_portion else 0
    #         self.sodium_per_gram = (self.sodium_per_portion / self.grams_portion) if self.sodium_per_portion else 0
    #
    #     except ZeroDivisionError:
    #         self.calories_per_gram = self.protein_per_gram = self.carbs_per_gram = self.fats_per_gram = 0
    #         self.fiber_per_gram = self.sodium_per_gram = 0
    #
    #     super().save(*args, **kwargs)


    def __str__(self):
        return self.name
