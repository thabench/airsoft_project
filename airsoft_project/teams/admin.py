from django.contrib import admin
from teams.models import Player, Team, Profile

# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('n_name', 'team', 'date_of_birth')
    
    
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts')
    
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_organizer', 'is_player')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Profile, ProfileAdmin)