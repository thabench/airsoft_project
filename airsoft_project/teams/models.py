from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    n_name = models.CharField('Nickname of the player', max_length=150)
    team = models.OneToOneField("Team", on_delete=models.SET_NULL, default='No team')
    games_played = models.IntegerField()
    player_from = models.CharField('Town where player is from')
    date_of_birth = models.DateField()
    team_leader = models.BooleanField()
        
    class Meta:
        verbose_name = _("Player")
        verbose_name_plural = _("Players")

    def __str__(self):
        return f'{self.n_name} ({self.team})'
    
    
class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique player ID')
    name = models.CharField('Name of the Team', max_length=150)
    contacts = models.CharField('contacts', max_length=150)
    players = models.ForeignKey("Player", on_delete=models.SET_NULL, null=True, blank=True)
        
    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk": self.pk})