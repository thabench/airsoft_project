from django import views
from django.urls import path, include
from events import views

urlpatterns = [
    path('', views.index, name='events_index'),
    path('list/', views.EventListView.as_view(), name='event_list'),
]
