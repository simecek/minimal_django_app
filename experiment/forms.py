# experiment/forms.py

from django import forms
from .models import ExperimentResult

class ExperimentResultForm(forms.ModelForm):
    class Meta:
        model = ExperimentResult
        fields = ['ProteinName', 'Chromosome', 'Start', 'Stop']

