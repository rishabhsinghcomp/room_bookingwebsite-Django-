# Generated by Django 4.0.4 on 2022-04-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='date_time',
        ),
        migrations.AddField(
            model_name='rooms',
            name='date',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rooms',
            name='timeslots',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
