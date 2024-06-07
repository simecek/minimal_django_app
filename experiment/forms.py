# experiment/forms.py

from django import forms
from .models import ExperimentResult

class ExperimentResultForm(forms.ModelForm):
    ProteinName = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    Chromosome = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    Start = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    Stop = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = ExperimentResult
        fields = ['ProteinName', 'Chromosome', 'Start', 'Stop']
