# Generated by Django 5.1 on 2024-09-22 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_rename_enrollment_date_enrollment_enrolled_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Enrollment',
        ),
    ]