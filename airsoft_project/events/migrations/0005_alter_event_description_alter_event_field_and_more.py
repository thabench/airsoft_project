# Generated by Django 4.0.6 on 2022-08-21 12:06

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('events', '0004_alter_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=tinymce.models.HTMLField(help_text='Field', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='field',
            field=models.ForeignKey(help_text='Field', null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.field'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(help_text='Organizer', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_organizers', to='events.organizer'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'active'), ('i', 'inactive')], default='a', help_text='Status', max_length=1),
        ),
        migrations.AlterField(
            model_name='field',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Organizer', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='field_organizers', to='events.organizer'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='profile',
            field=models.OneToOneField(help_text='Profile', on_delete=django.db.models.deletion.CASCADE, related_name='organizer', to='teams.profile'),
        ),
    ]
