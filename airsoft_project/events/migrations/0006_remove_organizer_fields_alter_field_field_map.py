# Generated by Django 4.0.6 on 2022-07-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_field_field_map'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizer',
            name='fields',
        ),
        migrations.AlterField(
            model_name='field',
            name='field_map',
            field=models.ImageField(null=True, upload_to='events/static/maps', verbose_name='Image of the map'),
        ),
    ]