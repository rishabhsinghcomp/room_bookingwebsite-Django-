# Generated by Django 4.0.4 on 2022-04-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_remove_rooms_date_time_rooms_date_rooms_timeslots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='date',
            field=models.CharField(default='main', max_length=100),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='timeslots',
            field=models.CharField(default='main', max_length=100),
        ),
    ]
