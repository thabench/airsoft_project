# Generated by Django 4.0.6 on 2022-08-04 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_alter_player_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='picture',
            new_name='p_picture',
        ),
    ]