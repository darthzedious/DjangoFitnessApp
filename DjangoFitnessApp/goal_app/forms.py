from django import forms

from DjangoFitnessApp.goal_app.models import Goal
from DjangoFitnessApp.mixins import PlaceholderMixin


class GoalForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Goal
        fields = ["weight", "height", "age", "gender", "activity", "goal_weight", "goal_type"]
        widgets = {
            "gender": forms.Select(attrs={
                "class": "form-control",
            }),
            "activity": forms.Select(attrs={
                "class": "form-control",
            }),
            "goal_type": forms.Select(attrs={
                "class": "form-control",
            }),
        }
