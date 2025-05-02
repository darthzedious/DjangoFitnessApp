from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView

from DjangoFitnessApp.trainings_app.choices import WorkoutTypeChoices
from DjangoFitnessApp.trainings_app.forms import TrainingSessionForm, TrainingSessionDeleteForm
from DjangoFitnessApp.trainings_app.models import TrainingSession, Exercise


class TrainingsView(ListView):
    """A list view that displays all the training session the user has."""

    template_name = "training/training_templates/training_template.html"
    context_object_name = "trainings"
    model = TrainingSession
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get("search", '')
        type_filter = self.request.GET.get("type", '')

        queryset = TrainingSession.objects.all()

        if search_query:
            queryset = queryset.filter(
                Q(workout_type__icontains=search_query) |
                Q(gym__icontains=search_query) |
                Q(date__icontains=search_query)
            )

        if type_filter:
            queryset = queryset.filter(workout_type=type_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query_dict = self.request.GET.copy()
        if 'page' in query_dict:
            query_dict.pop('page')
        context['query_string'] = urlencode(query_dict)

        context['selected_type'] = self.request.GET.get('type', '')
        context['session_pk'] = self.kwargs.get('session_pk') #if session_pk else None (if accessed to create trainexercise)
        context['all_types'] = WorkoutTypeChoices.choices  # Pass types to template
        return context


class TrainingCreateView(LoginRequiredMixin, CreateView):
    """Create a new training session."""
    template_name = "training/training_templates/training_create_template.html"
    model = TrainingSession
    form_class = TrainingSessionForm

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'training_details',
            kwargs={
                'pk': self.object.pk
            }
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Workout'
        return context


class TrainingDetailsView(LoginRequiredMixin, DetailView):
    """Load the details template for the chosen training session."""
    template_name = "training/training_templates/training_details_template.html"
    model = TrainingSession
    context_object_name = "training"


class TrainingUpdateView(LoginRequiredMixin, UpdateView):
    """Edit the training session information."""
    form_class = TrainingSessionForm
    template_name = "training/training_templates/training_create_template.html"

    def get_queryset(self):
        return TrainingSession.objects.filter(profile=self.request.user.profile)

    def get_success_url(self):
        return reverse_lazy(
            "training_details",
            kwargs={'pk': self.object.training_session.pk}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Workout'
        return context


#TODO create TrainingDeleteView

class TrainingDeleteView(LoginRequiredMixin, FormView, DeleteView):
    form_class = TrainingSessionDeleteForm
    template_name = "training/training_templates/training_delete_template.html"
    model = TrainingSession
    success_url = reverse_lazy('trainings')

    def get_form_kwargs(self):
        """Prefills the form with data."""
        kwargs = super().get_form_kwargs()
        workout = get_object_or_404(TrainingSession, pk=self.kwargs['pk'])
        kwargs['instance'] = workout
        return kwargs

    def get_context_data(self, **kwargs):
        """Update context data sent to the template."""
        context = super().get_context_data(**kwargs)
        context['training_session'] = get_object_or_404(
            TrainingSession,
            pk=self.object.pk,
        )
        return context
