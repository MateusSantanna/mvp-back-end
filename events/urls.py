from django.urls import path
from .views import list_events, event_detail

urlpatterns = [
    path('events/', list_events),
    path('events/<str:id>/', event_detail),
]