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
        fields = ['meal', 'meal_type', 'grams']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.initial.get('meal'):
            self.fields['meal'].widget.attrs['readonly'] = True
