from django.db import models


class ActivityChoices(models.TextChoices):
    SEDENTARY = "Sedentary", "Little or no exercise"
    LIGHT = "Light activity", "Light exercise/sports 1-3 days/week"
    MODERATE = "Moderate", "Moderate exercise/sports 3-5 days/week"
    ACTIVE = "Active", "Hard exercise/sports 6-7 days a week"
    VERY_ACTIVE = "Very active", "Very hard exercise or physical job"


class GoalChoices(models.TextChoices):
    EXTREME_GAIN = "Extreme Gain", "Extreme Weight Gain (+1000 kcal)"
    GAIN = "Gain", "Weight Gain (+500 kcal)"
    MILD_GAIN = "Mild Gain", "Mild Weight Gain (+250 kcal)"
    MAINTAIN = "Maintain", "Maintain Weight"
    MILD_LOSS = "Mild Loss", "Mild Weight Loss (-250 kcal)"
    LOSS = "Loss", "Weight Loss (-500 kcal)"
    EXTREME_LOSS = "Extreme Loss", "Extreme Weight Loss (-1000 kcal)"

