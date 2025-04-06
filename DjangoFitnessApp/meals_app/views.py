from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, TemplateView, DetailView

from DjangoFitnessApp.meals_app.choices import MealCategoryChoices, MealType
from DjangoFitnessApp.meals_app.forms import DailyMealForm, MealForm
from DjangoFitnessApp.meals_app.models import DailyMeal, Meal, DailyConsumption


class CategoryDisplayView(LoginRequiredMixin, TemplateView):
    """Display a template with all the meal categories."""
    template_name = "meals/meal/category_list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = dict(MealCategoryChoices.choices)

        context["categories"] = categories

        return context


class MealsListView(LoginRequiredMixin, ListView):
    """Displays all the meals from the selected category."""
    model = Meal
    context_object_name = "meals"
    template_name = "meals/meal/meals_list.html"
    paginate_by = 10

    def get_queryset(self):
        category = self.kwargs.get("category")
        search_query = self.request.GET.get("search", '')

        queryset = Meal.objects.filter(category__iexact=category)

        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) | Q(brand__icontains=search_query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs.get("category")

        return context


class MealCreateView(LoginRequiredMixin, CreateView):
    """Create a new meal."""
    template_name = 'meals/meal/create_new_meal.html'
    model = Meal
    form_class = MealForm

    def get_success_url(self):
        return reverse_lazy(
            'meal-details',
            kwargs={'pk': self.object.pk}
        )

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


class MealDetailView(LoginRequiredMixin, DetailView):
    template_name = 'meals/meal/meal_details.html'
    model = Meal
    context_object_name = "meal"


class DailyMealListView(LoginRequiredMixin, ListView):
    template_name = 'meals/daily_meal/diet_plan.html'
    model = DailyMeal

    def get_queryset(self):
        """The meals for the current day."""
        return DailyMeal.objects.filter(profile=self.request.user.profile, date=date.today()).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user.profile
        goal = profile.goal.last()

        daily_calories = goal.daily_calories if profile.goal.exists() else 0
        daily_consumption, created = DailyConsumption.objects.get_or_create(profile=profile, date=date.today())

        # created=False if data already exists;
        if not created:
            DailyConsumption.objects.update_totals(daily_consumption)

        remaining_calories = daily_calories - daily_consumption.total_calories

        context['consumed_calories'] = daily_consumption.total_calories
        context['remaining_calories'] = remaining_calories
        context['daily_calories'] = daily_calories
        context['goal'] = goal
        context['daily_consumption'] = daily_consumption
        context['meal_types'] = dict(MealType.choices)

        return context


class DailyMealCreateView(LoginRequiredMixin, CreateView):
    """
    This view calculates and saves the data for each meal the user submits for the day.
    """
    template_name = 'meals/daily_meal/add_dailymeal.html'
    form_class = DailyMealForm
    success_url = reverse_lazy('diet-tracker')

    def get_initial(self):
        """Prefill meal from URL parameters."""
        initial = super().get_initial()
        meal_id = self.request.GET.get('meal_id')

        if meal_id:
            meal = get_object_or_404(Meal, id=meal_id)
            initial['meal'] = meal

        return initial


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
        form.instance.sodium = (form.instance.meal.sodium_per_gram or 0) * form.instance.grams

        return super().form_valid(form)


class DailyMealDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete the chosen meal from the DB. After that redirect to DailyMealListView
    where the daily statistics get updated automatically."""
    model = DailyMeal
    template_name = 'meals/daily_meal/delete_dailymeal.html'
    success_url = reverse_lazy('diet-tracker')

    def test_func(self):
        goal = get_object_or_404(DailyMeal, pk=self.kwargs["pk"])
        return self.request.user == goal.profile.user


class DailyMealHistoryView(LoginRequiredMixin, ListView):
    template_name = "meals/daily_meal/daily_meal_history.html"
    context_object_name = "daily_consumptions"
    paginate_by = 2

    def get_queryset(self):
        """Retrieve DailyConsumption entries for the logged-in user, ordered by date (most recent first)."""
        return DailyConsumption.objects.filter(profile=self.request.user.profile).order_by("-date")

    def get_context_data(self, **kwargs):
        """Add meal details to paginated DailyConsumption entries."""
        context = super().get_context_data(**kwargs)

        history_data = {}
        for data in context["daily_consumptions"]: # context["object_list"]
            date_str = data.date.strftime("%Y-%m-%d")  # Format date as string

            # Fetch meals for this specific day
            meals = DailyMeal.objects.filter(profile=self.request.user.profile, date=data.date).order_by("meal_type")

            # Saves macronutrient values for each meal [{"id": meal.id,}, {"id": meal.id,}, {"id": meal.id,}]
            meal_data = []
            for meal in meals:
                meal_data.append({
                    "id": meal.id,
                    "name": meal.meal.name,
                    "meal_type": meal.meal_type,
                    "grams": meal.grams,
                    "calories": meal.calories,
                    "protein": meal.protein,
                    "carbs": meal.carbs,
                    "fats": meal.fats,
                })

            history_data[date_str] = {
                "total_calories": data.total_calories,
                "total_protein": data.total_protein,
                "total_carbs": data.total_carbs,
                "total_fats": data.total_fats,
                "total_fiber": data.total_fiber,
                "total_sodium": data.total_sodium,
                "meals": meal_data,  #  contains the data for every meal added for that day
            }

        context["history_data"] = history_data
        return context


def copy_meal(request, meal_id):
    meal = get_object_or_404(DailyMeal, id=meal_id)

    DailyMeal.objects.create(
        profile=meal.profile,
        date=date.today(),
        meal=meal.meal,
        grams=meal.grams,
        meal_type=meal.meal_type,
        calories=meal.calories,
        protein=meal.protein,
        carbs=meal.carbs,
        sugars=meal.sugars,
        fats=meal.fats,
        saturated_fats=meal.saturated_fats,
        fiber=meal.fiber,
        sodium=meal.sodium,
    )

    return redirect('diet-tracker')
