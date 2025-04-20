from django.urls import path

from . import views

urlpatterns = [
    path("", views.TrainingsView.as_view(), name="trainings"),
    path("create-new-workout/", views.TrainingCreateView.as_view(), name="training_create"),
    path("workout-details/<int:pk>/", views.TrainingDetailsView.as_view(), name="training_details"),
    path("workout-edit/<int:pk>/", views.TrainingUpdateView.as_view(), name="training_edit"),

    path("exercise-create/", views.ExerciseCreateView.as_view(), name="exercise_create"),

    path("exercise-list/", views.ExerciseListView.as_view(), name="exercise_list"),
    path("exercise-list/<int:session_pk>/", views.ExerciseListView.as_view(), name="exercise_list-select"),

    path("exercise-details/<int:pk>/", views.ExerciseDetailsView.as_view(), name="exercise_details"),


    path(
        "training-exercise-create/<int:session_pk>/",
         views.TrainingExerciseCreateView.as_view(),
         name="training_exercise_create",
         ),
    path(
    "training-exercise-create/<int:session_pk>/<int:exercise_pk>/",
        views.TrainingExerciseCreateView.as_view(),
        name="training_exercise_create_with_exercise"
    ),

    path('training-exercise-edit/<int:pk>/', views.TrainingExerciseUpdateView.as_view(), name="training_exercise_edit"),

    path(
        'training/<int:training_session_pk>/exercise/<int:training_exercise_pk>/set/add/',
        views.SetLogCreateView.as_view(),
        name='setlog_create'
    ),

    path('set/<int:pk>/edit/', views.SetlogUpdateView.as_view(), name="setlog_update"),
    path('set/<int:pk>/delete/', views.SetLogDeleteView.as_view(), name="setlog_delete"),

]