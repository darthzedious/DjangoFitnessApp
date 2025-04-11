from django.contrib import admin
from DjangoFitnessApp.goal_app.models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = (
        "profile", "weight", "height", "age", "gender", "activity",
        "goal_type", "daily_calories", "daily_protein", "daily_carbohydrates",
        "daily_fats",
    )

    list_filter = (
        "profile", "gender", "activity", "goal_type",
    )

    search_fields = (
        "profile", "age",
    )
