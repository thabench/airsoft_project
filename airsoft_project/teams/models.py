from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from django.utils.translation import gettext_lazy as _
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_organizer = models.BooleanField(default=False)
    is_player = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user}'


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique player ID')
    name = models.CharField('Name of the Team', max_length=150)
    contacts = models.CharField('contacts', max_length=150)
    
    @classmethod
    def get_default_pk(cls):
        team, created = cls.objects.get_or_create(
            name='No Team', defaults=dict(contacts='-'))
        return team.pk
        
    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk": self.pk})
    
    
class Player(models.Model):
    profile = models.OneToOneField('Profile', related_name='player',on_delete=models.CASCADE, null=True, blank=True)
    n_name = models.CharField('Nickname of the player', max_length=150, default="New Player")
    picture = models.ImageField(default="defaulf.png", upload_to="profile_pics/")
    team = models.ForeignKey('Team', related_name='players', on_delete=models.SET_NULL, null=True, default=Team.get_default_pk)
    events = models.ManyToManyField("events.Event", related_name='registered_players', blank=True)
    games_played = models.IntegerField(null=True, blank=True, default=0)
    player_from = models.CharField('Town where player is from', max_length=150)
    date_of_birth = models.DateField(null=True, blank=True)
    team_leader = models.BooleanField(default=False)
        
    class Meta:
        verbose_name = _("Player")
        verbose_name_plural = _("Players")

    def __str__(self):
        return f'{self.n_name} ({self.team})'
    
    def get_absolute_url(self):
        return reverse("player_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.picture.path)       
