from django.shortcuts import render, redirect
from django.views import generic
from teams.models import Player, Team
from events.models import Organizer
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.forms import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from airsoft_project.forms import UserUpdateForm, PlayerUpdateForm, OrganizerUpdateForm

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
    
    
class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'player_detail.html'
    
    
class TeamDetailView(generic.DetailView):
    model = Team
    template_name = 'team_detail.html'
    
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
                    print(organizer)
                    print(player)
                    new_user = User.objects.create_user(username=username, email=email, password=password)
                    if organizer == 'on':
                        new_user.profile.is_organizer = True
                        new_user.profile.save()
                        print(f'--{new_user.username}--')
                        print(f'-is org-{new_user.profile.is_organizer}--')
                        Organizer.objects.create(profile=new_user.profile)
                    if player == 'on':
                        new_user.profile.is_player = True
                        new_user.profile.save()
                        print(f'--{new_user.username}--')
                        print(f'-is play-{new_user.profile.is_player}--')
                        Player.objects.create(profile=new_user.profile)     
                    elif organizer != 'on' and player != 'on':
                        new_user.profile.is_player = True
                        new_user.profile.save()
                        Player.objects.create(profile=new_user.profile)
                    messages.success(request, _('Registration successful!'))
                    return redirect('login')
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
        if u_form.is_valid() and o_form.is_valid():
            u_form.save()
            o_form.save()
            p_form.save()
            messages.success(request, f"Profile updated")
            return redirect('profile')
    elif request.method == "POST" and current_user.profile.is_organizer == True:
        o_form = OrganizerUpdateForm(request.POST, request.FILES, instance=request.user.profile.organizer)
        if u_form.is_valid() and o_form.is_valid():
            u_form.save()
            o_form.save()
            messages.success(request, f"Profile updated")
            return redirect('profile')
    elif request.method == "POST" and current_user.profile.is_player == True:
        p_form = PlayerUpdateForm(request.POST, request.FILES, instance=request.user.profile.player)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile updated")
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


# @login_required
# def profile(request):
#     current_user = request.user
#     u_form = UserUpdateForm(request.POST, instance=request.user)
#     if request.method == "POST" and current_user.profile.organizer:
#         o_form = OrganizerUpdateForm(request.POST, request.FILES, instance=request.user.profile.organizer)
#         if u_form.is_valid() and o_form.is_valid():
#             u_form.save()
#             o_form.save()
#             messages.success(request, f"Profile updated")
#             return redirect('profile')
#     if request.method == "POST" and current_user.profile.player:
#         p_form = PlayerUpdateForm(request.POST, request.FILES, instance=request.user.profile.player)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f"Profile updated")
#             return redirect('profile')    
#     else:
        
#         if current_user.profile.is_organizer == True:
#             u_form = UserUpdateForm(instance=request.user)
#             o_form = OrganizerUpdateForm(instance=request.user.profile.organizer)
            
#             context = {
#             'u_form': u_form,
#             'o_form': o_form
#             }
            
#         elif current_user.profile.is_player == True:
#             u_form = UserUpdateForm(instance=request.user)
#             p_form = PlayerUpdateForm(instance=request.user.profile.player)
        
#             context = {
#             'u_form': u_form,
#             'p_form': p_form,
#             }
            
#         else:
#             context = {
#             'u_form': u_form,
#             }
            
#     return render(request, 'profile.html', context)