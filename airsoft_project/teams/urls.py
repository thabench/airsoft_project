from django import views
from django.urls import path, include
from teams import views

urlpatterns = [
    path('', views.TeamListView.as_view(), name='teams'),
    path('create_team', views.create_team, name='create_team'),
    path('<uuid:pk>', views.TeamDetailView.as_view(), name='team_detail'),
    path('<uuid:pk>/update_team', views.TeamUpdateView.as_view(), name='update_team'),
    path('<uuid:pk>/delete_team', views.delete_team, name='delete_team'),
    path('<uuid:pk>/join_team', views.join_team, name='join_team'),
    path('<uuid:pk>/leave_team', views.leave_team, name='leave_team'),
    path('players/', views.PlayerListView.as_view(), name='players'),
    path('players/<int:pk>', views.PlayerDetailView.as_view(), name='player_detail'),
    path('players/register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
