# Generated by Django 4.0.6 on 2022-08-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, default='12:00 PM', null=True, verbose_name='Time of event'),
        ),
    ]