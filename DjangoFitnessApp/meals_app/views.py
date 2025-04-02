from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, TemplateView

from DjangoFitnessApp.meals_app.choices import MealCategoryChoices
from DjangoFitnessApp.meals_app.forms import DailyMealForm, MealForm
from DjangoFitnessApp.meals_app.models import DailyMeal, Meal


class CategoryDisplayView(LoginRequiredMixin, TemplateView):
    """Display a template with all the meal categories."""
    template_name = "meals/category_list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = [category for c, category in MealCategoryChoices.choices]

        context["categories"] = categories

        return context

class MealsListView(LoginRequiredMixin, ListView):
    """Displays all the meals from the selected category."""
    model = Meal
    context_object_name = "meals"
    template_name = "meals/meals_list.html"

    def get_queryset(self):
        category = self.kwargs.get("category")
        queryset = Meal.objects.filter(category__iexact=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs.get("category")

        return context



class DailyMealListView(LoginRequiredMixin, ListView):
    template_name = 'meals/diet_plan.html'
    model = DailyMeal

    def get_queryset(self):
        return DailyMeal.objects.filter(profile=self.request.user.profile, date=date.today()).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user.profile
        goal = profile.goal.last()
        # goal = getattr(profile, 'goal', None)

        daily_calories = goal.daily_calories if profile.goal.exists() else 0
        consumed_calories = sum(daily_meal.meal.calories_per_gram * daily_meal.grams for daily_meal in self.get_queryset())
        remaining_calories = daily_calories - consumed_calories

        context['daily_calories'] = daily_calories
        context['consumed_calories'] = consumed_calories
        context['remaining_calories'] = remaining_calories

        return context


class DailyMealCreateView(LoginRequiredMixin, CreateView):
    template_name = 'meals/add_meal.html'
    form_class = DailyMealForm
    success_url = reverse_lazy('diet-tracker')


    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        form.instance.date = date.today()

        form.instance.calories = (form.instance.meal.calories_per_gram or 0) * form.instance.grams
        form.instance.protein = (form.instance.meal.protein_per_gram or 0) * form.instance.grams

        form.instance.carbs = (form.instance.meal.carbs_per_gram or 0) * form.instance.grams
        form.instance.sugars = (form.instance.meal.sugars_per_gram or 0) * form.instance.grams

        form.instance.fats = (form.instance.meal.fats_per_gram or 0) * form.instance.grams
        form.instance.saturated_fats = (form.instance.meal.saturated_fats_per_gram or 0) * form.instance.grams

        form.instance.fiber = (form.instance.meal.fiber_per_gram or 0) * form.instance.grams
        form.instance.sodium = (form.instance.meal.sodium_per_gram or 0)* form.instance.grams

        return super().form_valid(form)


class MealCreateView(LoginRequiredMixin, CreateView):
    """Create a new meal."""
    template_name = 'meals/create_new_meal.html'
    model = Meal
    form_class = MealForm
    success_url = reverse_lazy('diet-tracker')

    def form_valid(self, form):
        form.instance.calories_per_gram = form.instance.calories_per_portion / form.instance.grams_portion
        form.instance.protein_per_gram = form.instance.protein_per_portion / form.instance.grams_portion

        form.instance.carbs_per_gram = form.instance.carbs_per_portion / form.instance.grams_portion
        form.instance.sugars_per_gram = (form.instance.sugars_per_portion or 0) / form.instance.grams_portion

        form.instance.fats_per_gram = form.instance.fats_per_portion / form.instance.grams_portion
        form.instance.saturated_fats_per_gram = (form.instance.saturated_fats_per_portion or 0) / form.instance.grams_portion

        form.instance.fiber_per_gram = (form.instance.fiber_per_portion or 0) / form.instance.grams_portion
        form.instance.sodium_per_gram = (form.instance.sodium_per_portion or 0) / form.instance.grams_portion


        return super().form_valid(form)


class DailyMealDeleteView(LoginRequiredMixin, DeleteView):
    model = DailyMeal
    template_name = 'meals/delete_meal.html'
    success_url = reverse_lazy('diet-tracker')
