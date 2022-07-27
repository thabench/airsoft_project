from django import views
from django.urls import path, include
from events import views

urlpatterns = [
    path('', views.index, name='events_index'),
    path('list/', views.EventListView.as_view(), name='event_list'),
    path('list/<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
    path('fields/', views.FieldListView.as_view(), name='field_list'),
    path('fields/<int:pk>', views.FieldDetailView.as_view(), name='field_detail'),
    path('organizers/', views.OrganizerListView.as_view(), name='organizer_list'),
    path('organizers/<int:pk>', views.OrganizerDetailView.as_view(), name='organizer_detail'),
]
