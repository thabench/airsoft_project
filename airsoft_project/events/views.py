from django.shortcuts import render
from django.views import generic
from events.models import Organizer, Event, Field
import airsoft_project.forms as my_forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime

# Create your views here.


def index(request):
    current_month = datetime.now().month
    events = Event.objects.filter(status='a')
    context = {'events': events,
               'current_month': current_month,
               }
    
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
    
########### EVENT MANAGEMENT

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
    form_class = my_forms.OrganizerEventCreateForm
    success_url = "/events/list/"
    template_name = 'organizer_event_form.html'
    
    def form_valid(self, form):
        form.instance.organizer = self.request.user.profile.organizer
        return super().form_valid(form)
    

class OrganizerEventUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Event
    form_class = my_forms.OrganizerEventUpdateForm
    success_url = "/events/list/"
    template_name = 'organizer_update_event_form.html'
    
    def form_valid(self, form):
        form.instance.organizer = self.request.user.profile.organizer
        return super().form_valid(form)
    
    def test_func(self):
        event = self.get_object()
        return self.request.user == event.organizer.profile.user
    
    
class OrganizerEventDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Event
    success_url = "/events/list/"
    template_name = 'organizer_delete_event.html'

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.organizer.profile.user
    
    
########### FIELD MANAGEMENT

class OrganizerFieldListView(LoginRequiredMixin, generic.ListView):
    model = Field
    context_object_name = 'fields'
    template_name = 'organizer_fields.html'

    def get_queryset(self):
        return Field.objects.filter(created_by=self.request.user.profile.organizer)
    
    
class OrganizerFieldDetailView(LoginRequiredMixin, generic.DetailView):
    model = Field
    context_object_name = 'field'
    template_name = 'organizer_field.html'
    
    
class OrganizerFieldCreateView(LoginRequiredMixin, generic.CreateView):
    model = Field
    success_url = "/events/fields/"
    template_name = 'organizer_field_form.html'
    form_class = my_forms.OrganizerFieldForm
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user.profile.organizer
        print('form valid')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print('form invalid')
        return super().form_invalid(form)
    

class OrganizerFieldUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Field
    success_url = "/events/fields/"
    template_name = 'organizer_update_field_form.html'
    form_class = my_forms.OrganizerFieldForm
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user.profile.organizer
        print('form valid')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print('form invalid')
        return super().form_invalid(form)
    
    def test_func(self):
        field = self.get_object()
        return self.request.user == field.created_by.profile.user
    
    
class OrganizerFieldDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Field
    success_url = "/events/fields/"
    template_name = 'organizer_delete_field.html'

    def test_func(self):
        field = self.get_object()
        return self.request.user == field.created_by.profile.user