# Generated by Django 5.1 on 2024-09-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('student', 'Student')], default='student', max_length=10),
        ),
    ]