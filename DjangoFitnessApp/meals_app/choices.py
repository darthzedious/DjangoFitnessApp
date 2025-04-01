from django.db import models


class MealCategoryChoices(models.TextChoices):
    MY_MEALS = "my_meals", "My Meals"
    PORK = "Pork", "Pork"
    BEEF = "Beef", "Beef"
    POULTRY = "Poultry", "Poultry"
    SEAFOOD = "Seafood", "Seafood"
    FAST_FOOD = "Fast_Food", "Fast Food"
    DAIRY = "Dairy", "Dairy"
    CEREAL = "cereal", "Cereal, Grains & Pasta"
    FRUITS = "Fruits", "Fruits"
    VEGETABLES = "Vegetables", "Vegetables"
    SWEETS = "Sweets", "Sweets & Snacks"
    DRINKS = "Drinks", "Drinks"
    OTHER = "Other", "Other"


class MealType(models.TextChoices):
    BREAKFAST = "breakfast", "Breakfast"
    LUNCH = "lunch", "Lunch"
    DINNER = "dinner", "Dinner"
    SNACK = "snack", "Snack"
