from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from DjangoFitnessApp.trainings_app.forms import TrainingSessionForm
from DjangoFitnessApp.trainings_app.models import TrainingSession


class TrainingsView(ListView):
    """A list view that displays all the training session the user has."""

    template_name = "training/training_templates/training_template.html"
    context_object_name = "trainings"
    model = TrainingSession
    paginate_by = 10


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


#TODO create TrainingDeleteView
