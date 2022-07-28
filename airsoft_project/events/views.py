from django.shortcuts import render
from django.views import generic
from events.models import Organizer, Event, Field

# Create your views here.


def index(request):
    events = Event.objects.all()
    # active_events = Event.objects.filter(status='a')
    
    context = {'events': events,
               
               } #'active_events': active_events,
    
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')


class EventListView(generic.ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event_list.html'
    

class FieldListView(generic.ListView):
    model = Field
    context_object_name = 'fields'
    template_name = 'field_list.html'
    
    
class OrganizerListView(generic.ListView):
    model = Organizer
    context_object_name = 'organizers'
    template_name = 'organizer_list.html'
    

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'event_detail.html'
    
    
class FieldDetailView(generic.DetailView):
    model = Field
    template_name = 'field_detail.html'
    
    
class OrganizerDetailView(generic.DetailView):
    model = Organizer
    template_name = 'organizer_detail.html'