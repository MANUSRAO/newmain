# Generated by Django 4.1.6 on 2023-02-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0008_student_onholiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='endDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='numberOfDays',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
