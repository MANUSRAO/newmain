# Generated by Django 4.1.6 on 2023-02-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0003_alter_student_blood_alter_student_branch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AlterField(
            model_name='student',
            name='usn',
            field=models.CharField(blank=True, max_length=12, primary_key=True, serialize=False),
        ),
    ]
