# Generated by Django 4.0.6 on 2022-08-11 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import teams.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique player ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Name of the Team')),
                ('contacts', models.CharField(max_length=150, verbose_name='contacts')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_organizer', models.BooleanField(default=False)),
                ('is_player', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_name', models.CharField(default='New Player', max_length=150, verbose_name='Nickname of the player')),
                ('picture', models.ImageField(default='defaulf.png', upload_to='profile_pics/')),
                ('games_played', models.IntegerField(blank=True, default=0, null=True)),
                ('player_from', models.CharField(max_length=150, verbose_name='Town where player is from')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('team_leader', models.BooleanField(default=False)),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='teams.profile')),
                ('team', models.ForeignKey(default=teams.models.Team.get_default_pk, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_players', to='teams.team')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
    ]
