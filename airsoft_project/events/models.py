from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

# Create your models here.

class Organizer(models.Model):
    name = models.CharField('Name of the organizer', max_length=150)
    email = models.EmailField('Email of organizer', max_length=150, null=True)
    contacts = models.CharField('Address and contacts', max_length=150)
    description = HTMLField(null=True)
    
        
    class Meta:
        verbose_name = _("Organizer")
        verbose_name_plural = _("Organizers")

    def __str__(self):
        return self.name
    
    
class Event(models.Model):
    name = models.CharField('Name of the event',  max_length=150)
    date = models.DateTimeField('Date of event', null=True, blank=True)
    organizer = models.ForeignKey("Organizer", related_name='event_organizers', on_delete=models.SET_NULL, null=True)
    field = models.ForeignKey('Field', on_delete=models.SET_NULL, null=True)
    description = HTMLField(null=True)
    price = models.FloatField("Price")
    max_players = models.IntegerField("Maximum player number")
    registered_players  = models.IntegerField("Registered player number")
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})
    
    
class Field(models.Model):
    name = models.CharField('Name of the game field',  max_length=150)
    location_long = models.CharField('Location longitude', max_length=50, null=True)
    location_lat = models.CharField('Location latitude', max_length=50, null=True)
    description = HTMLField(null=True)
    field_map = models.ImageField('Image of the map', upload_to='events/static/maps', null=True)
    
    class Meta:
        verbose_name = _("Field")
        verbose_name_plural = _("Fields")

    def __str__(self):
        return self.name
    
    @property
    def get_api_key(self):
        from airsoft_project.settings import GOOGLE_MAPS_API_KEY as api_key
        return api_key