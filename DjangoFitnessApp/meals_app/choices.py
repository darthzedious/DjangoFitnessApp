from django.db import models


class MealCategoryChoices(models.TextChoices):
    MY_MEALS = "My Meals", "My Meals"
    PORK = "Pork", "Pork"
    BEEF = "Beef", "Beef"
    POULTRY = "Poultry", "Poultry"
    SEAFOOD = "Seafood", "Seafood"
    FAST_FOOD = "Fast Food", "Fast Food"
    DAIRY = "Dairy", "Dairy"
    CEREAL = "Cereal, Grains & Pasta", "Cereal, Grains & Pasta"
    FRUITS = "Fruits", "Fruits"
    VEGETABLES = "Vegetables", "Vegetables"
    SWEETS = "Sweets & Snacks", "Sweets & Snacks"
    DRINKS = "Drinks", "Drinks"
    OTHER = "Other", "Other"


class MealType(models.TextChoices):
    BREAKFAST = "Breakfast", "Breakfast"
    LUNCH = "Lunch", "Lunch"
    DINNER = "Dinner", "Dinner"
    SNACK = "Snack", "Snack"
