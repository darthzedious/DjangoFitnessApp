from django.urls import path

from DjangoFitnessApp.home_app.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]