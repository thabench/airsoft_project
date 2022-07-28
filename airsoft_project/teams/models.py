from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    n_name = models.CharField('Nickname of the player', max_length=150)
    picture = models.ImageField(default="profile_pics/defaulf.png", upload_to="profile_pics")
    team = models.ForeignKey("Team", related_name='team_players', on_delete=models.SET_NULL, null=True)
    games_played = models.IntegerField(null=True, blank=True)
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
    
    
class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique player ID')
    name = models.CharField('Name of the Team', max_length=150)
    contacts = models.CharField('contacts', max_length=150)
    # players = models.ManyToManyField("Player", related_name='players', blank=True)
        
    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk": self.pk})