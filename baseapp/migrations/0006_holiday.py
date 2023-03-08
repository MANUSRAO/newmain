# Generated by Django 4.1.6 on 2023-02-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0005_magstaff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(max_length=12)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField(null=True)),
                ('numberOfDays', models.IntegerField(null=True)),
            ],
        ),
    ]
