# Generated by Django 4.1.5 on 2023-03-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentprofile',
            name='Department',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
