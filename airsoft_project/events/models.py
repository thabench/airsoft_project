from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Organizer(models.Model):
    name = models.CharField('Name of the organizer', max_length=150)
    contacts = models.CharField('Address and contacts', max_length=150)
    events = models.ForeignKey('Event', related_name='event', on_delete=models.SET_NULL, null=True, blank=True)
    fields = models.ForeignKey('Field', related_name='field', on_delete=models.SET_NULL, null=True, blank=True)
        
    class Meta:
        verbose_name = _("Organizer")
        verbose_name_plural = _("Organizers")

    def __str__(self):
        return self.name
    
    
class Event(models.Model):
    name = models.CharField('Name of the event',  max_length=150)
    date = models.DateTimeField('Date of event', null=True, blank=True)
    field = models.OneToOneField('Field', on_delete=models.SET_NULL, null=True)
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
    location = models.CharField('Location coordinates', max_length=50)
    field_map = models.ImageField('Image of the map', upload_to='events/static/maps', null=True)
    
    class Meta:
        verbose_name = _("Field")
        verbose_name_plural = _("Fields")

    def __str__(self):
        return self.name