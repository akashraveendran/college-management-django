# Generated by Django 4.1.5 on 2023-03-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsAndInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(choices=[('News', 'News'), ('Other Informations', 'Other Informations')], max_length=255)),
                ('Title', models.CharField(max_length=255)),
                ('Content', models.CharField(max_length=255)),
                ('uploaded_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
