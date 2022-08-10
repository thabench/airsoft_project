from django.shortcuts import render
from django.views import generic
from events.models import Organizer, Event, Field
from airsoft_project.forms import OrganizerEventCreateForm, OrganizerEventUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    
    
class OrganizerEventCreateView(LoginRequiredMixin, generic.CreateView):
    model = Event
    form_class = OrganizerEventCreateForm
    success_url = "/events/list/"
    template_name = 'organizer_event_form.html'
    
    def form_valid(self, form):
        form.instance.organizer = self.request.user.profile.organizer
        return super().form_valid(form)
    

class OrganizerEventUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Event
    form_class = OrganizerEventUpdateForm
    success_url = "/events/list/"
    template_name = 'organizer_update_event_form.html'
    
    def form_valid(self, form):
        form.instance.organizer = self.request.user.profile.organizer
        return super().form_valid(form)
    
    def test_func(self):
        event = self.get_object()
        return self.request.user == event.organizer.profile.user