# Generated by Django 5.0.6 on 2024-06-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProteinName', models.CharField(max_length=255)),
                ('ProteinLink', models.URLField(blank=True, null=True)),
                ('Chromosome', models.CharField(max_length=255)),
                ('Start', models.IntegerField()),
                ('Stop', models.IntegerField()),
                ('Strand', models.CharField(max_length=1)),
                ('Score', models.FloatField()),
                ('Notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]