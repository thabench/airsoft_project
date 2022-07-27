from django import views
from django.urls import path, include
from teams import views

urlpatterns = [
    path('', views.TeamListView.as_view(), name='teams'),
    path('<uuid:pk>', views.TeamDetailView.as_view(), name='team_detail'),
    path('players/', views.PlayerListView.as_view(), name='players'),
    path('players/<int:pk>', views.PlayerDetailView.as_view(), name='player_detail'),
]
