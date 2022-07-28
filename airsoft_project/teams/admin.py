from django.contrib import admin
from teams.models import Player, Team 

# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'n_name', 'team', 'date_of_birth')
    
    
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)