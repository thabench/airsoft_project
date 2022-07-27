# Generated by Django 4.0.6 on 2022-07-27 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_remove_team_players_team_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='players',
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_players', to='teams.team'),
        ),
    ]
