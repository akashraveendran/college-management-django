# Generated by Django 4.1.5 on 2023-03-23 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester', models.CharField(choices=[('semester 1', 'semester 1'), ('semester 2', 'semester 2'), ('semester 3', 'semester 3'), ('semester 4', 'semester 4'), ('semester 5', 'semester 5'), ('semester 6', 'semester 6')], max_length=255)),
                ('Department', models.CharField(choices=[('Computer Science Engineerning', 'Computer Science Engineerning'), ('Electronics Engineerning', 'Electronics Engineerning'), ('Civil Engineerning', 'Civil Engineerning'), ('Mechanical Engineerning', 'Mechanical Engineerning'), ('Electrical Engineerning', 'Electrical Engineerning')], max_length=255)),
                ('Register_Number', models.CharField(max_length=255)),
                ('Date_of_birth', models.DateField()),
                ('Phone_Number', models.IntegerField()),
                ('Address', models.CharField(max_length=255)),
                ('Profile_Image', models.FileField(upload_to='students')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]