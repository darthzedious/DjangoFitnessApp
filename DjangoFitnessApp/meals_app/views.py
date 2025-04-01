from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from DjangoFitnessApp.meals_app.forms import DailyMealForm, MealForm
from DjangoFitnessApp.meals_app.models import DailyMeal, Meal


class DailyMealListView(LoginRequiredMixin, ListView):
    template_name = 'meals/diet_plan.html'
    model = DailyMeal


    def get_queryset(self):
        return DailyMeal.objects.filter(profile=self.request.user.profile, date=date.today())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user.profile
        goal = profile.goal.last()

        daily_calories = goal.daily_calories if profile.goal.exists() else 0
        # consumed_calories = sum(meal.meal.calories_per_gram * meal.grams for meal in self.get_queryset())
        # remaining_calories = max(0, daily_calories - consumed_calories)
        #
        context['daily_calories'] = daily_calories
        # context['consumed_calories'] = consumed_calories
        # context['remaining_calories'] = max(0, remaining_calories)
        # context['form'] = DailyMealForm()

        return context


class DailyMealCreateView(LoginRequiredMixin, CreateView):
    template_name = 'meals/add_meal.html'
    form_class = DailyMealForm
    success_url = reverse_lazy('diet-tracker')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        form.instance.date = date.today()

        return super().form_valid(form)


class MealCreateView(LoginRequiredMixin, CreateView):
    template_name = 'meals/create_new_meal.html'
    model = Meal
    form_class = MealForm
    success_url = reverse_lazy('diet-tracker')




class DailyMealDeleteView(LoginRequiredMixin, DeleteView):
    model = DailyMeal
    template_name = 'meals/delete_meal.html'
    success_url = reverse_lazy('diet-tracker')
