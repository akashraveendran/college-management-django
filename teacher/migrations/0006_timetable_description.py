# Generated by Django 4.1.5 on 2023-03-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_academicwork_total_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='Description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
