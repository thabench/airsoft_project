from django.contrib import admin
from events.models import Organizer, Event, Field

# Register your models here.

admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(Field)