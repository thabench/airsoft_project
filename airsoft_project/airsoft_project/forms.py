from teams.models import Player, Team
from events.models import Organizer, Event, Field
from django import forms
from django.contrib.auth.models import User
        

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email',]


class PlayerUpdateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['n_name', 'date_of_birth', 'player_from', 'picture',]
        widgets = {'date_of_birth': forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))}
        

class OrganizerUpdateForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name', 'contacts', 'description', 'profile_picture',]
        
        
class OrganizerEventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'time', 'field', 'description', 'price', 'max_players',]
        widgets = {'date': forms.DateInput(attrs={'type': 'date'}),
                   'time': forms.TimeInput(attrs={'type': 'time'})}
        
        
class OrganizerEventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'time', 'field', 'description', 'price', 'max_players']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'}),
                   'time': forms.TimeInput(attrs={'type': 'time'})}
        
        
class OrganizerFieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['name', 'location_long', 'location_lat', 'description','field_map', 'created_by']   
        widgets = {'created_by': forms.HiddenInput()}

class TeamUpdateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'contacts', 'emblem',]