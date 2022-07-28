# Generated by Django 4.0.6 on 2022-07-28 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0013_alter_player_games_played_alter_player_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='team_leader',
            field=models.BooleanField(default=False),
        ),
    ]
