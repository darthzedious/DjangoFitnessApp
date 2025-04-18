from django.urls import path

from DjangoFitnessApp.trainings_app import views

urlpatterns = [
    path("trainings/", views.TrainingsView.as_view(), name="trainings"),
]