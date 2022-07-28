from django.shortcuts import render, redirect
from django.views import generic
from teams.models import Player, Team
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.forms import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

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
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']    
        password2 = request.POST['password2']
        ok_password = pattern.findall(password)
        if not ok_password:
            messages.error(request, _(f'Password must be at least 8 symbols and it must have at least one capital letter and number'))
            return redirect('register')
        
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, _(f'User name {username} is already taken!'))
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, _(f'Email {email} already exists!'))
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.success(request, _('Registration successful!'))
                    return redirect('login')
        else:
            messages.error(request, _('Passwords did not match!'))
            return redirect('register')
    return render(request, 'register.html')

@login_required
def profile(request):
    return render(request, 'profile.html')