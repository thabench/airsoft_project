# Generated by Django 4.0.6 on 2022-08-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='name',
            field=models.CharField(default='New Organizer', max_length=150, verbose_name='Name of the organizer'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='profile_picture',
            field=models.ImageField(default='events/static/media/defaulf.png', upload_to='events/static/organizer_pics'),
        ),
    ]
