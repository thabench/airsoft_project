from teams.models import Player
from events.models import Organizer
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