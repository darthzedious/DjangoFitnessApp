from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from DjangoFitnessApp.trainings_app.choices import ExerciseTypeChoices
from DjangoFitnessApp.trainings_app.forms import ExerciseForm
from DjangoFitnessApp.trainings_app.models import Exercise


class ExerciseCreateView(LoginRequiredMixin, CreateView):
    """Create a new exercise in the database so the user can use it as training exercise."""
    form_class = ExerciseForm
    model = Exercise
    template_name = "training/exercise_templates/exercise_create_template.html"

    def get_success_url(self):
        return reverse_lazy(
            'training_details',
            kwargs={
                'pk': self.object.pk
            }
        )

class ExerciseListView(LoginRequiredMixin, ListView):
    template_name = "training/exercise_templates/exercise_list_template.html"
    context_object_name = "exercises"
    paginate_by = 1

    def get_queryset(self):
        """Get the queryset with the objects that will be displayed in the list view.
        Has a search form in the template that sends filter parameter to the "search_query".
        Has a filter buttons that send a parameter for the "type_filter".
        """
        search_query = self.request.GET.get("search", '')
        type_filter = self.request.GET.get("type", '')

        queryset = Exercise.objects.all()
        #
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(equipment_brand__icontains=search_query) |
                Q(exercise_type__icontains=search_query)
            )

        if type_filter:
            queryset = queryset.filter(exercise_type=type_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query_dict = self.request.GET.copy()
        if 'page' in query_dict:
            query_dict.pop('page')
        context['query_string'] = urlencode(query_dict)

        context['selected_type'] = self.request.GET.get('type', '')
        context['session_pk'] = self.kwargs.get('session_pk') #if session_pk else None (if accessed to create trainexercise)
        context['all_types'] = ExerciseTypeChoices.choices  # Pass types to template
        return context


class ExerciseDetailsView(LoginRequiredMixin, DetailView):
    """Load the details for the chosen exercise."""
    template_name = 'training/exercise_templates/exercise_details.html'
    model = Exercise
    context_object_name = "exercise"