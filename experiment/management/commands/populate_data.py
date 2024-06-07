# experiment/management/commands/populate_data.py

from django.core.management.base import BaseCommand
from experiment.models import ExperimentResult
import random

class Command(BaseCommand):
    help = 'Populate the database with sample experiment results'

    def handle(self, *args, **kwargs):
        for i in range(100):
            ExperimentResult.objects.create(
                ProteinName=f'Protein_{i}',
                ProteinLink=f'http://example.com/protein_{i}',
                Chromosome=f'chr{i % 23 + 1}',
                Start=random.randint(1, 1000000),
                Stop=random.randint(1000001, 2000000),
                Strand='+' if i % 2 == 0 else '-',
                Score=random.uniform(0, 1),
                Notes=f''
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))
