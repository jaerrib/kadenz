# Generated by Django 4.2.3 on 2023-07-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='street',
            field=models.TextField(blank=True),
        ),
    ]
