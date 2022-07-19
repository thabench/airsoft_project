from django.shortcuts import render
from django.views import generic
from teams.models import Player, Team

# Create your views here.

def index(request):
    
    return render(request, 'index.html')


class PlayerListView(generic.ListView):
    model = Player
    context_object_name = 'players'
    template_name = 'players.html'
   
    
class TeamListView(generic.ListView):
    model = Team
    context_object_name = 'teams'
    template_name = 'teams.html'