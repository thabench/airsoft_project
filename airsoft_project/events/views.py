from django.shortcuts import render
from django.views import generic
from events.models import Organizer, Event, Field
from teams.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

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
    

class OrganizerEventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'organizer_events.html'

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user.profile.organizer)
    
    
class OrganizerEventDetailView(LoginRequiredMixin, generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'organizer_event.html'