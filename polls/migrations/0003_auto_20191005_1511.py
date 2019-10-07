# Generated by Django 2.2.6 on 2019-10-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_dl_model_satisfaction_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='dl_model',
            name='Work_accident',
            field=models.IntegerField(blank=True, default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='dl_model',
            name='average_montly_hours',
            field=models.IntegerField(blank=True, default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='dl_model',
            name='department',
            field=models.IntegerField(blank=True, default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='dl_model',
            name='last_evaluation',
            field=models.IntegerField(blank=True, default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='dl_model',
            name='left',
            field=models.IntegerField(blank=True, default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='dl_model',
            name='number_project',
            field=models.IntegerField(blank=True, default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='dl_model',
            name='promotion_last_5years',
            field=models.IntegerField(blank=True, default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='dl_model',
            name='salary',
            field=models.IntegerField(blank=True, default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='dl_model',
            name='time_spend_company',
            field=models.IntegerField(blank=True, default=1, max_length=200),
        ),
    ]
