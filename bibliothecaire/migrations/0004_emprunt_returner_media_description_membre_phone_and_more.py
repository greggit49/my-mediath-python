# Generated by Django 5.1.7 on 2025-03-25 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0003_remove_media_date_emprunt_remove_media_emprunteur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprunt',
            name='returner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='media',
            name='description',
            field=models.TextField(blank=True, default='', max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='membre',
            name='phone',
            field=models.CharField(default='0746764646', max_length=10),
        ),
        migrations.AlterField(
            model_name='emprunt',
            name='date_emprunt',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='emprunt',
            name='date_retour',
            field=models.DateField(default=datetime.date(2024, 11, 20)),
        ),
        migrations.AlterField(
            model_name='membre',
            name='bloque',
            field=models.BooleanField(default=False),
        ),
    ]
