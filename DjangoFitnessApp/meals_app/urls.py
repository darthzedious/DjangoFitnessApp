from django.urls import path

from DjangoFitnessApp.meals_app import views

urlpatterns = [
    path('diet-tracker/', views.DailyMealListView.as_view(), name='diet-tracker'),
    path('add-meal/', views.DailyMealCreateView.as_view(), name='add-meal'),
    path('create-new-meal/', views.MealCreateView.as_view(), name='create-new-meal'),
    path('delete-meal/<int:pk>/', views.DailyMealDeleteView.as_view(), name='delete-meal'),
    path('category-list/', views.CategoryDisplayView.as_view(), name='category-list'),
    path('meals/<str:category>/', views.MealsListView.as_view(), name='meals-list'),
    path('meal-details/<int:pk>/', views.MealDetailView.as_view(), name='meal-details'),
    path('daily-meal-history/', views.DailyMealHistoryView.as_view(), name='daily-meal-history'),
    path('copy_meal/<int:meal_id>/', views.copy_meal, name='copy_meal'),
]