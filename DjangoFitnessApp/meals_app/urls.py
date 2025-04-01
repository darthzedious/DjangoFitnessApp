from django.urls import path

from DjangoFitnessApp.meals_app import views

urlpatterns = [
    path('diet-tracker/', views.DailyMealListView.as_view(), name='diet-tracker'),
    path('add-meal/', views.DailyMealCreateView.as_view(), name='add-meal'),
    path('create-new-meal/', views.MealCreateView.as_view(), name='create-new-meal'),
    path('delete-meal/<int:pk>/', views.DailyMealDeleteView.as_view(), name='delete-meal'),
]