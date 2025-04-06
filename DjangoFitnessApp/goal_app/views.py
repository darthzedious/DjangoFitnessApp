from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView

from DjangoFitnessApp.goal_app.forms import GoalForm
from DjangoFitnessApp.goal_app.models import Goal


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = GoalForm
    template_name = "goal/goal_form.html"

    def form_valid(self, form):
        if not hasattr(self.request.user, "profile"):
            return self.form_invalid(form)

        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "goal-detail",
            kwargs={
                "pk": self.object.pk
            }
        )


class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = "goal/goal_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "goal-detail",
            kwargs={
                "pk": self.object.pk
            }
        )


class GoalDetailView(LoginRequiredMixin, DetailView):
    """Loads the most recent goal added. Set and accessible in profile template."""
    model = Goal
    template_name = "goal/goal_details.html"


class GoalListView(LoginRequiredMixin, ListView):
    model = Goal
    template_name = "goal/goal_list.html"
    context_object_name = "goals"
    paginate_by = 3

    def get_queryset(self):
        return Goal.objects.filter(profile=self.request.user.profile).order_by("-id")


class GoalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Goal
    template_name = "goal/goal_delete.html"
    success_url = reverse_lazy("goal-list")

    def test_func(self):
        goal = get_object_or_404(Goal, pk=self.kwargs["pk"])
        return self.request.user == goal.profile.user
