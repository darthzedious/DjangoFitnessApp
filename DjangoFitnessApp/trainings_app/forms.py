from django import forms

from DjangoFitnessApp.mixins import DisabledReadonlyMixin
from DjangoFitnessApp.trainings_app.models import Exercise, TrainingSession, TrainingExercise, SetLog


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'


class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        exclude = ('profile',)
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'workout_type': forms.Select(attrs={'class': 'form-select'}),
        }


class TrainingSessionDeleteForm(DisabledReadonlyMixin, TrainingSessionForm):
    pass


class TrainingExerciseForm(forms.ModelForm):
    class Meta:
        model = TrainingExercise
        exclude = ('training_session', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.initial.get('exercise'):
            self.fields['exercise'].disabled = True


class TrainingExerciseDeleteForm(DisabledReadonlyMixin, TrainingExerciseForm):
    pass


class SetLogForm(forms.ModelForm):
    class Meta:
        model = SetLog
        exclude = ('training_exercise',)


class SetLogDeleteForm(DisabledReadonlyMixin, SetLogForm):
    pass

