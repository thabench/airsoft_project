from django import views
from django.urls import path, include
from events import views

urlpatterns = [
    path('', views.index, name='events_index'),
    path('list/', views.EventListView.as_view(), name='event_list'),
    path('list/<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
    path('list/<int:pk>/register', views.register_to_event, name='register_to_event'),
    path('fields/', views.FieldListView.as_view(), name='field_list'),
    path('fields/<int:pk>', views.FieldDetailView.as_view(), name='field_detail'),
    path('organizers/', views.OrganizerListView.as_view(), name='organizer_list'),
    path('organizers/<int:pk>', views.OrganizerDetailView.as_view(), name='organizer_detail'),
    path('about', views.about, name='about'),
    path('my_events', views.OrganizerEventListView.as_view(), name='organizer_events'),
    path('my_events/<int:pk>', views.OrganizerEventDetailView.as_view(), name='organizer_event'),
    path('my_events/new', views.OrganizerEventCreateView.as_view(), name='create_event'),
    path('my_events/<int:pk>/update', views.OrganizerEventUpdateView.as_view(), name='update_event'),
    path('my_events/<int:pk>/delete', views.OrganizerEventDeleteView.as_view(), name='delete_event'),
    path('my_fields', views.OrganizerFieldListView.as_view(), name='organizer_fields'),
    path('my_fields/<int:pk>', views.OrganizerFieldDetailView.as_view(), name='organizer_field'),
    path('my_fields/new', views.OrganizerFieldCreateView.as_view(), name='create_field'),
    path('my_fields/<int:pk>/update', views.OrganizerFieldUpdateView.as_view(), name='update_field'),
    path('my_fields/<int:pk>/delete', views.OrganizerFieldDeleteView.as_view(), name='delete_field'),
]
