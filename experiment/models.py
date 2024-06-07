# experiment/models.py

from django.db import models

class ExperimentResult(models.Model):
    ProteinName = models.CharField(max_length=255)
    ProteinLink = models.URLField(blank=True, null=True)
    Chromosome = models.CharField(max_length=255)
    Start = models.IntegerField()
    Stop = models.IntegerField()
    Strand = models.CharField(max_length=1)
    Score = models.FloatField()
    Notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ProteinName

