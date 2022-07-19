from django import views
from django.urls import path, include
from events import views

urlpatterns = [
    path('', views.index, name='events_index')
]
