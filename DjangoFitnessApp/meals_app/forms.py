from django import forms
from .models import Meal, DailyMeal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = [
            'name', 'brand', 'description', 'category',
            'calories_per_portion', "grams_portion",
            'fats_per_portion',
            'saturated_fats_per_portion',
            'carbs_per_portion',
            'sugars_per_portion',
            'protein_per_portion',
            'fiber_per_portion',
            'sodium_per_portion',
            'meal_picture',
        ]

class DailyMealForm(forms.ModelForm):
    class Meta:
        model = DailyMeal
        fields = [
            'meal',
            'meal_type',
            'grams',
        ]


class DailyMealDeleteForm(forms.ModelForm):
    # Define fields to display consumption data (readonly)
    total_calories = forms.FloatField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    total_protein = forms.FloatField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    total_carbs = forms.FloatField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    total_fats = forms.FloatField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = DailyMeal
        fields = []
#
# class MealSearchForm(forms.Form):
#     query = forms.CharField(
#         max_length=100,
#         required=False,
#         label="Search Meal"
#     )

