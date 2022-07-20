from django.shortcuts import render
from django.views import generic
from events.models import Organizer, Event, Field

# Create your views here.


def index(request):
    
    return render(request, 'index.html')


class EventListView(generic.ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event_list.html'