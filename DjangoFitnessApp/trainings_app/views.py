# from urllib.parse import urlencode
#
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.db.models import Q
# from django.shortcuts import get_object_or_404
# from django.urls import reverse_lazy
# from django.views.generic import ListView, CreateView, DetailView, UpdateView
#
# from DjangoFitnessApp.trainings_app.choices import ExerciseTypeChoices
# from DjangoFitnessApp.trainings_app.forms import TrainingSessionForm, ExerciseForm, TrainingExerciseForm
# from DjangoFitnessApp.trainings_app.models import TrainingSession, Exercise, TrainingExercise
#
#
# class TrainingsView(ListView):
#     template_name = "training/training_templates/training_template.html"
#     context_object_name = "trainings"
#     model = TrainingSession
#     paginate_by = 10
#
#
# class TrainingCreateView(LoginRequiredMixin, CreateView):
#     template_name = "training/training_templates/training_create_template.html"
#     model = TrainingSession
#     form_class = TrainingSessionForm
#
#     def form_valid(self, form):
#         form.instance.profile = self.request.user.profile
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy(
#             'training_details',
#             kwargs={
#                 'pk': self.object.pk
#             }
#         )
#
# class TrainingDetailsView(LoginRequiredMixin, DetailView):
#     template_name = "training/training_templates/training_details_template.html"
#     model = TrainingSession
#     context_object_name = "training"
#
#
# class TrainingUpdateView(LoginRequiredMixin, UpdateView):
#     form_class = TrainingSessionForm
#     template_name = "training/training_templates/training_create_template.html"
#
#
#     def get_queryset(self):
#         return TrainingSession.objects.filter(profile=self.request.user.profile)
#
#     def get_success_url(self):
#         return reverse_lazy(
#             "training_details",
#             kwargs={'pk': self.object.pk}
#         )
#
# #TODO create TrainingDeleteView
#
#
# class ExerciseCreateView(LoginRequiredMixin, CreateView):
#     form_class = ExerciseForm
#     model = Exercise
#     template_name = "training/exercise_templates/exercise_create_template.html"
#
#     def get_success_url(self):
#         return reverse_lazy(
#             'training_details',
#             kwargs={
#                 'pk': self.object.pk
#             }
#         )
#
# class ExerciseListView(LoginRequiredMixin, ListView):
#     template_name = "training/exercise_templates/exercise_list_template.html"
#     context_object_name = "exercises"
#     paginate_by = 1
#
#     def get_queryset(self):
#         search_query = self.request.GET.get("search", '')
#         type_filter = self.request.GET.get("type", '')
#
#         queryset = Exercise.objects.all()
#         #
#         if search_query:
#             queryset = queryset.filter(
#                 Q(name__icontains=search_query) |
#                 Q(equipment_brand__icontains=search_query) |
#                 Q(exercise_type__icontains=search_query)
#             )
#
#         if type_filter:
#             queryset = queryset.filter(exercise_type=type_filter)
#
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         query_dict = self.request.GET.copy()
#         if 'page' in query_dict:
#             query_dict.pop('page')
#         context['query_string'] = urlencode(query_dict)
#
#         context['selected_type'] = self.request.GET.get('type', '')
#         context['session_pk'] = self.kwargs.get('session_pk')
#         context['all_types'] = ExerciseTypeChoices.choices  # Pass types to template
#         return context
#
#
# class ExerciseDetailsView(LoginRequiredMixin, DetailView):
#     template_name = 'training/exercise_templates/exercise_details.html'
#     model = Exercise
#     context_object_name = "exercise"
#
#
# class TrainingExerciseCreateView(LoginRequiredMixin, CreateView):
#     form_class = TrainingExerciseForm
#     template_name = 'training/training_exercise_templates/training_exercise_create.html'
#     model = TrainingExercise
#
#     def dispatch(self, request, *args, **kwargs):
#         self.training_session = get_object_or_404(
#             TrainingSession,
#             pk=kwargs['session_pk'],
#             profile=request.user.profile
#         )
#
#         self.exercise=None
#         if 'exercise_pk' in kwargs:
#             self.exercise = get_object_or_404(
#                 Exercise,
#                 pk=kwargs['exercise_pk'],
#             )
#
#         return super().dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         """Assign the training session of the current exercise to selected session."""
#         form.instance.training_session = self.training_session
#
#         return super().form_valid(form)
#
#
#     def get_success_url(self):
#         """Use to redirect to the current training session."""
#         return reverse_lazy(
#             'training_details',
#             kwargs={'pk': self.training_session.pk}
#         )
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['training_session'] = self.training_session
#         return context
#
#     def get_initial(self):
#         """Use to prefill the exercise field in the form."""
#         initial = super().get_initial()
#         if self.exercise:
#             initial['exercise'] = self.exercise
#         return initial
#
#
#
