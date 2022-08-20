from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from teams.models import Profile
from PIL import Image
from datetime import datetime, date
import pytz
utc=pytz.UTC

# Create your models here.

class Organizer(models.Model):
    profile = models.OneToOneField(Profile, related_name='organizer',on_delete=models.CASCADE)
    name = models.CharField('Name of the organizer', max_length=150, default='New Organizer')
    profile_picture = models.ImageField(default="default.png", upload_to="organizer_pics/")
    contacts = models.CharField('Address and contacts', max_length=150)
    description = HTMLField(null=True)
    
        
    class Meta:
        verbose_name = _("Organizer")
        verbose_name_plural = _("Organizers")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
    
    
class Event(models.Model):
    name = models.CharField('Name of the event',  max_length=150)
    date = models.DateField('Date of event', null=True, blank=True)
    time = models.TimeField('Time of event', null=True, blank=True, help_text='i.e.: 12:00 PM')
    organizer = models.ForeignKey("Organizer", related_name='event_organizers', on_delete=models.SET_NULL, null=True)
    field = models.ForeignKey('Field', on_delete=models.SET_NULL, null=True)
    description = HTMLField(null=True)
    price = models.FloatField("Price")
    max_players = models.IntegerField("Maximum player number")
    created_on = models.DateTimeField(auto_now_add=True)
    
    EVENT_STATUS = (
        ('a', 'active'),
        ('i', 'inactive'),
    )
    
    status = models.CharField(max_length=1, choices=EVENT_STATUS, blank=True, default='a', help_text='Status',)
    
    class Meta:
        ordering = ['-date']
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    @property
    def is_active(self):
        if self.date < date.today():
            self.status = 'i'
            return self.save()
        elif self.date > date.today():
            self.status = 'a'
            self.save()
            return True 
    
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})
    
    
class Field(models.Model):
    name = models.CharField('Name of the game field',  max_length=150)
    location_long = models.FloatField('Location longitude', max_length=50, null=True)
    location_lat = models.FloatField('Location latitude', max_length=50, null=True)
    description = HTMLField(null=True, blank=True)
    field_map = models.ImageField(default="default_map.png", upload_to="maps/")
    created_by = models.ForeignKey("Organizer", related_name='field_organizers', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = _("Field")
        verbose_name_plural = _("Fields")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("field_detail", kwargs={"pk": self.pk})
    
    @property
    def get_api_key(self):
        from airsoft_project.settings import GOOGLE_MAPS_API_KEY as api_key
        return api_key