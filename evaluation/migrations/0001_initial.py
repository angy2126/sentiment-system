# Generated by Django 5.1.3 on 2024-11-16 02:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.EmailField(max_length=254)),
                ('course_year', models.CharField(max_length=100)),
                ('likert_answers', models.JSONField()),
                ('choice_question', models.CharField(choices=[('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')], max_length=10)),
                ('comments', models.TextField(blank=True, null=True)),
                ('suggestions', models.TextField(blank=True, null=True)),
                ('is_submitted', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='evaluation.event')),
            ],
        ),
        migrations.CreateModel(
            name='SentimentAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('neutral_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('negative_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentiments', to='evaluation.evaluation')),
            ],
        ),
    ]