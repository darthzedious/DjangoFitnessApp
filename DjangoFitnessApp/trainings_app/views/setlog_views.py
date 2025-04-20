#TODO create SetLogCreateView, SetLogUpdateView, SetLogDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from DjangoFitnessApp.trainings_app.forms import SetLogForm
from DjangoFitnessApp.trainings_app.models import SetLog, TrainingExercise, TrainingSession


class SetLogCreateView(LoginRequiredMixin, CreateView):
    form_class = SetLogForm
    template_name = 'training/setlog_templates/setlog_create_template.html'
    model = SetLog

    def dispatch(self, request, *args, **kwargs):
        self.training_exercise = get_object_or_404(
            TrainingExercise,
            pk=kwargs['training_exercise_pk'],
        )
        self.training_session = self.training_exercise.training_session

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.training_exercise = self.training_exercise
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'training_details',
            kwargs={
                'pk': self.training_exercise.training_session.pk
            },
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['training_session'] = self.training_session
        context['training_exercise'] = self.training_exercise

        return context


class SetlogUpdateView(LoginRequiredMixin, UpdateView):
    form_class = SetLogForm
    template_name = 'training/setlog_templates/setlog_create_template.html'
    model = SetLog

    def get_success_url(self):
        return reverse_lazy(
            'training_details',
            kwargs={
                'pk': self.object.training_exercise.training_session.pk
            }
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['training_session'] = get_object_or_404(
            TrainingSession,
            pk=self.object.training_exercise.training_session.pk,
        )
        return context


class SetLogDeleteView(LoginRequiredMixin, DeleteView):
    model = SetLog
    form_class = SetLogForm
    template_name = 'training/setlog_templates/setlog_create_template.html'

    def get_success_url(self):
        return reverse_lazy(
            'training_details',
            kwargs={
                'pk': self.object.training_exercise.training_session.pk
            }
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['training_session'] = get_object_or_404(
            TrainingSession,
            pk=self.object.training_exercise.training_session.pk,
        )
        return context
