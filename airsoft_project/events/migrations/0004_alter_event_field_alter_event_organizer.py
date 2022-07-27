# Generated by Django 4.0.6 on 2022-07-27 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_field_location_field_location_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.field'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.organizer'),
        ),
    ]