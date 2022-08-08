# Generated by Django 4.0.6 on 2022-08-08 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_alter_player_games_played_alter_player_n_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='n_name',
            field=models.CharField(default=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='teams.profile'), max_length=150, verbose_name='Nickname of the player'),
        ),
    ]
