from teams.models import Player
from events.models import Organizer
from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class PlayerUpdateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['n_name', 'picture', 'player_from', 'date_of_birth']
        

class OrganizerUpdateForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name', 'picture', 'contacts', 'description']