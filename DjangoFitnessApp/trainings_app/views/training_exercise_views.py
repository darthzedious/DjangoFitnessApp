from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from DjangoFitnessApp.trainings_app.forms import TrainingExerciseForm
from DjangoFitnessApp.trainings_app.models import TrainingExercise, TrainingSession, Exercise


class TrainingExerciseCreateView(LoginRequiredMixin, CreateView):
    """
    Add an exercise to recently selected training session.
    Get the training session id from the exercises table for the logged user.
    Gets the chosen exercise by the id from the exercises table.(variables from the url passed from the templates)
    """

    form_class = TrainingExerciseForm
    template_name = 'training/training_exercise_templates/training_exercise_create.html'
    model = TrainingExercise

    def dispatch(self, request, *args, **kwargs):
        self.training_session = get_object_or_404(
            TrainingSession,
            pk=kwargs['session_pk'],
            profile=request.user.profile
        )

        self.exercise=None
        if 'exercise_pk' in kwargs:
            self.exercise = get_object_or_404(
                Exercise,
                pk=kwargs['exercise_pk'],
            )

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Assign the training session of the current exercise to selected session."""
        form.instance.training_session = self.training_session

        return super().form_valid(form)

    def get_success_url(self):
        """Use to redirect to the current training session."""
        return reverse_lazy(
            'training_details',
            kwargs={'pk': self.training_session.pk}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['training_session'] = self.training_session
        return context

    def get_initial(self):
        """Use to prefill the exercise field in the form."""
        initial = super().get_initial()
        if self.exercise:
            initial['exercise'] = self.exercise
        return initial


class TrainingExerciseUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TrainingExerciseForm
    template_name = 'training/training_exercise_templates/training_exercise_create.html'

    def get_queryset(self):
        # Filter the queryset by the pk to get the specific TrainingExercise
        # Ensure the exercise belongs to the user's profile by filtering the training session.
        return TrainingExercise.objects.filter(
            training_session__profile=self.request.user.profile
        )

    def get_success_url(self):
        return reverse_lazy(
            'training_details',
            kwargs={'pk': self.object.training_session.pk}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['training_session'] = get_object_or_404(
            TrainingSession,
            pk=self.object.training_session.pk,
        )
        return context

#TODO create TrainingExerciseDeleteView, TrainingExerciseDisplayView