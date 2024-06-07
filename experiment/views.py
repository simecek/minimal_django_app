# experiment/views.py

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import ExperimentResult
from .forms import ExperimentResultForm

LIMIT = 50

def experiment_results(request):
    form = ExperimentResultForm(request.GET or None)
    results = ExperimentResult.objects.all()

    if form.is_valid():
        protein_name = form.cleaned_data.get('ProteinName')
        chromosome = form.cleaned_data.get('Chromosome')
        start = form.cleaned_data.get('Start')
        stop = form.cleaned_data.get('Stop')

        if protein_name:
            results = results.filter(ProteinName__icontains=protein_name)
        if chromosome:
            results = results.filter(Chromosome__iexact=chromosome)
        if start is not None:
            results = results.filter(Start__gte=start)
        if stop is not None:
            results = results.filter(Stop__lte=stop)

    paginator = Paginator(results, LIMIT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'results': page_obj,
        'total_results': paginator.count,
        'displayed_results': len(page_obj),
    }
    return render(request, 'experiment/experiment_results.html', context)
