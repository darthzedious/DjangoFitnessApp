"""
URL configuration for DjangoFitnessApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
       path('admin/', admin.site.urls),
    path('', include('DjangoFitnessApp.home_app.urls')),
    path('accounts/', include('DjangoFitnessApp.accounts.urls')),
    path('goals/', include('DjangoFitnessApp.goal_app.urls')),
    path('meals/', include('DjangoFitnessApp.meals_app.urls')),
    path('trainings/', include('DjangoFitnessApp.trainings_app.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
