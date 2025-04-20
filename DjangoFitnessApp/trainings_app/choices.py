from django.db import models


class WorkoutTypeChoices(models.TextChoices):
    CARDIO = 'cardio', 'Cardio'
    CHEST = 'chest', 'Chest'
    BACK = 'back', 'Back'
    SHOULDER = 'shoulder', 'Shoulder'
    ARMS = 'arms', 'Arms'
    LEGS = 'legs', 'Legs'
    FULL_BODY = 'full_body', 'Full Body'
    UPPER_BODY = 'upper_body', 'Upper Body'
    LOWER_BODY = 'lower_body', 'Lower Body'
    BODY_WEIGHT = 'body_weight', 'Body Weight'
    OTHER = 'other', 'Other'


class ExerciseTypeChoices(models.TextChoices):
    CARDIO = 'cardio', 'Cardio'
    MACHINE = 'machine', 'Machine'
    CABLE = 'cable', 'Cable'
    DUMBBELL = 'dumbbell', 'Dumbbell'
    FREE_WEIGHT = 'free_weight', 'Free Weight'
    BODY_WEIGHT = 'body_weight', 'Body Weight'
    OTHER = 'other', 'Other'
