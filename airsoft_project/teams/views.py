from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, get_list_or_404
from django.views import generic
from teams.models import Player, Team
from events.models import Organizer, Event
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.forms import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from airsoft_project.forms import UserUpdateForm, PlayerUpdateForm, OrganizerUpdateForm, TeamUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

# Create your views here.

class PlayerListView(generic.ListView):
    model = Player
    context_object_name = 'players'
    template_name = 'players.html'
    paginate_by = 4


class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'player_detail.html'   

    
class TeamListView(generic.ListView):
    model = Team
    context_object_name = 'teams'
    template_name = 'teams.html'
    paginate_by = 4
    
    
class TeamDetailView(generic.DetailView):
    model = Team
    template_name = 'team_detail.html'


class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Team
    form_class = TeamUpdateForm
    success_url = ""
    template_name = 'team_update_form.html'
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def test_func(self):
        team = self.get_object()
        return self.request.user.profile.player.team == team
        
    
@csrf_protect
def register(request):
    import re
    pattern = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')
    if request.method == "POST":
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']    
        password2 = request.POST['password2']
        organizer = request.POST.get('organizer', False)
        player = request.POST.get('player', False)
        
        ok_password = pattern.findall(password)
        if not ok_password:
            messages.error(request, _(f'Password must be at least 8 symbols and it must have at least one capital letter and number'))
            return redirect('register')
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, _(f'User name {username} is already taken!'))
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, _(f'Email {email} already exists!'))
                    return redirect('register')
                else:
                    new_user = User.objects.create_user(username=username, email=email, password=password)
                    if organizer == 'on':
                        new_user.profile.is_organizer = True
                        new_user.profile.save()
                        Organizer.objects.create(profile=new_user.profile)
                    if player == 'on':
                        new_user.profile.is_player = True
                        new_user.profile.save()
                        Player.objects.create(profile=new_user.profile)     
                    elif organizer != 'on' and player != 'on':
                        new_user.profile.is_player = True
                        new_user.profile.save()
                        Player.objects.create(profile=new_user.profile)
                    messages.success(request, _('Registration successful!'))
                    return redirect('profile')
        else:
            messages.error(request, _('Passwords did not match!'))
            return redirect('register')
    return render(request, 'register.html')


@login_required
def profile(request):
    current_user = request.user
    u_form = UserUpdateForm(request.POST, instance=request.user)
    if request.method == "POST" and current_user.profile.is_organizer == True and current_user.profile.is_player == True:
        o_form = OrganizerUpdateForm(request.POST, request.FILES, instance=request.user.profile.organizer)
        p_form = PlayerUpdateForm(request.POST, request.FILES, instance=request.user.profile.player)
        if u_form.is_valid() and o_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            o_form.save()
            
            messages.success(request, _(f"Profile updated"))
            return redirect('profile')
    elif request.method == "POST" and current_user.profile.is_organizer == True:
        o_form = OrganizerUpdateForm(request.POST, request.FILES, instance=request.user.profile.organizer)
        if u_form.is_valid() and o_form.is_valid():
            u_form.save()
            o_form.save()
            messages.success(request, _(f"Profile updated"))
            return redirect('profile')
    elif request.method == "POST" and current_user.profile.is_player == True:
        p_form = PlayerUpdateForm(request.POST, request.FILES, instance=request.user.profile.player)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, _(f"Profile updated"))
            return redirect('profile')    
    else:
        
        if current_user.profile.is_organizer == True and current_user.profile.is_player == True:
            u_form = UserUpdateForm(instance=request.user)
            o_form = OrganizerUpdateForm(instance=request.user.profile.organizer)
            p_form = PlayerUpdateForm(instance=request.user.profile.player)
            
            context = {
            'u_form': u_form,
            'o_form': o_form,
            'p_form': p_form,
            }
        elif current_user.profile.is_organizer == True:
            u_form = UserUpdateForm(instance=request.user)
            o_form = OrganizerUpdateForm(instance=request.user.profile.organizer)
            
            context = {
            'u_form': u_form,
            'o_form': o_form
            }
            
        elif current_user.profile.is_player == True:
            u_form = UserUpdateForm(instance=request.user)
            p_form = PlayerUpdateForm(instance=request.user.profile.player)
        
            context = {
            'u_form': u_form,
            'p_form': p_form,
            }
            
        else:
            u_form = UserUpdateForm(instance=request.user)
            context = {
            'u_form': u_form,
            }
            
    return render(request, 'profile.html', context)

@login_required
def create_team(request):
    if request.method == "POST":
        
        name = request.POST['name']
        contacts = request.POST['contacts']
        emblem = request.FILES['emblem']
        
        if Team.objects.filter(name=name).exists():
            messages.error(request, _(f'Team name {name} is already taken!'))
            return redirect('create_team')
        else:
            current_player = request.user.profile.player
            new_team = Team.objects.create(name=name, contacts=contacts, emblem=emblem)
            current_player.team = new_team
            current_player.team_leader = True
            current_player.save()
            messages.success(request, _('Team created!'))
            return redirect('teams')
    return render(request, 'create_team_form.html')


@login_required
def delete_team(request, pk):
    
    selected_team = get_object_or_404(Team, pk = pk)
    default_team = get_object_or_404(Team, name = 'No Team')
    context={'pk':pk,
             'team':selected_team,}
    
    if request.method == "POST":
        
        team_players = get_list_or_404(Player, team=selected_team)
        print(team_players)
        
        for player in team_players:
            player.team = default_team
            player.save()
        selected_team.delete()
        
        return redirect('teams')
    
    return render(request, "delete_team.html", context)


@login_required
def join_team(request, pk):
    
    selected_team = get_object_or_404(Team, pk = pk)
    player = request.user.profile.player
    context={'pk':pk,
             'team':selected_team,
             'player':player,}
    
    if request.method == "POST":
        player.team = selected_team
        player.team_leader = False
        if selected_team.players.count() == 0:
            player.team_leader = True
        player.save()
        
        return redirect('team_detail', pk=pk)
    
    return render(request, "join_team.html", context)


@login_required
def leave_team(request, pk):
    
    selected_team = get_object_or_404(Team, pk = pk)
    default_team = get_object_or_404(Team, name = 'No Team')
    player = request.user.profile.player
    context={'pk':pk,
             'team':selected_team,
             'player':player,}
    
    if request.method == "POST":
        player.team = default_team
        player.team_leader = False
        player.save()
        
        return redirect('team_detail', pk=pk)
    
    return render(request, "leave_team.html", context)


def search_teams(request):
    query = request.GET.get('query')
    search_results = Team.objects.filter(Q(name__icontains=query))
    return render(request, 'search_teams.html', {'teams': search_results, 'query': query})


def search_players(request):
    query = request.GET.get('query')
    search_results = Player.objects.filter(Q(n_name__icontains=query) | Q(team__name__icontains=query))
    return render(request, 'search_players.html', {'players': search_results, 'query': query})