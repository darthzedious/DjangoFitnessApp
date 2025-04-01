from django.urls import path

from . import views


urlpatterns = [
    path("goal/<int:pk>/", views.GoalDetailView.as_view(), name="goal-detail"),
    path("goal/<int:pk>/edit/", views.GoalUpdateView.as_view(), name="goal-update"),
    path("goal/create/", views.GoalCreateView.as_view(), name="goal-create"),
    path("goal/", views.GoalListView.as_view(), name="goal-list"),
    path('goal/delete/<int:pk>/', views.GoalDeleteView.as_view(), name='goal-delete'),
]
