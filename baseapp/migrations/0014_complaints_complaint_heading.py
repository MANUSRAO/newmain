# Generated by Django 4.1.6 on 2023-02-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0013_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='complaint_heading',
            field=models.CharField(default='Heading', max_length=50),
            preserve_default=False,
        ),
    ]
