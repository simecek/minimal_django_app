# experiment/urls.py

from django.urls import path
from .views import experiment_results

urlpatterns = [
    path('', experiment_results, name='experiment_results'),
]

