from django import views
from django.urls import path, include
from teams import views

urlpatterns = [
    path('', views.index, name='teams_index'),
    path('players/', views.PlayerListView.as_view(), name='players')
]
