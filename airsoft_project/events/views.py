from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from events.models import Organizer, Event, Field
import airsoft_project.forms as my_forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime
from django.db.models import Q

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
    paginate_by = 4
    

class FieldListView(generic.ListView):
    model = Field
    context_object_name = 'fields'
    template_name = 'field_list.html'
    paginate_by = 4
    
    
class OrganizerListView(generic.ListView):
    model = Organizer
    context_object_name = 'organizers'
    template_name = 'organizer_list.html'
    paginate_by = 4
    

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
    paginate_by = 4

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
    
    
class PlayerEventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'player_events.html'
    paginate_by = 4

    def get_queryset(self):
        return Event.objects.filter(registered_players=self.request.user.profile.player).filter(status = 'a')
 
 
class PlayerEventDetailView(LoginRequiredMixin, generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'player_event.html'
    

class PlayerCompletedEventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'player_completed_events.html'
    paginate_by = 4

    def get_queryset(self):
        return Event.objects.filter(registered_players=self.request.user.profile.player).filter(status = 'i')
 
 
class PlayerCompletedEventDetailView(LoginRequiredMixin, generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'player_completed_event.html'
    
    
class OrganizerFieldListView(LoginRequiredMixin, generic.ListView):
    model = Field
    context_object_name = 'fields'
    template_name = 'organizer_fields.html'
    paginate_by = 4

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
    
    
@login_required
def register_to_event(request, pk):
    
    selected_event = get_object_or_404(Event, pk = pk)
    player = request.user.profile.player
    context={'id':id,
             'event':selected_event,
             'player':player,}
    
    if request.method == "POST":
        player.events.add(selected_event)
        player.save()
        
        return redirect('event_detail', pk=pk)
    
    return render(request, "register_to_event.html", context)


def search_events(request):
    query = request.GET.get('query')
    search_results = Event.objects.filter(Q(name__icontains=query) | Q(organizer__name__icontains=query))
    return render(request, 'search_events.html', {'events': search_results, 'query': query})


def search_by_date(request):
    query = request.GET.get('query')
    search_results = Event.objects.filter(organizer=request.user.profile.organizer).filter(Q(date__contains=query))
    return render(request, 'search_events_by_date.html', {'events': search_results, 'query': query})