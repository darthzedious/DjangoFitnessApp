from django.contrib import admin
from DjangoFitnessApp.meals_app.models import Meal, DailyMeal, DailyConsumption


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = (
        "name", "brand", "category", "calories_per_portion", "grams_portion",
        "protein_per_portion", "carbs_per_portion", "fats_per_portion",
    )

    list_filter = (
        "category", "grams_portion",
    )

    search_fields = (
        "name", "brand",
    )


@admin.register(DailyMeal)
class DailyMealAdmin(admin.ModelAdmin):
    list_display = (
        "profile", "meal_type", "meal", "date",
        "grams", "calories",
    )

    list_filter = (
        "profile", "meal_type", "meal", "meal__brand",
    )

    search_fields = (
        "profile__first_name", "meal_type", "date", "meal__name", "meal__brand",
    )


@admin.register(DailyConsumption)
class DailyConsumptionAdmin(admin.ModelAdmin):
    list_display = (
        "profile", "date", "total_calories", "total_protein", "total_carbs", "total_fats",
    )

    list_filter = (
        "profile",
    )

    search_fields = (
        "profile__first_name", "date",
    )
