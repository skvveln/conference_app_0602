from django.urls import path
from events.views import EventDetailView, register_visitor

urlpatterns = [
    path('<int:pk>/', EventDetailView.as_view(), name = "event_detail"),
    path('register/<int:renginio_id>/', register_visitor, name = "register_visitor"),
]