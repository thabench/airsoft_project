# Generated by Django 4.0.6 on 2022-08-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_rename_o_picture_organizer_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='picture',
            field=models.ImageField(default='organizer_pics/defaulf.png', upload_to='organizer_pics'),
        ),
    ]
