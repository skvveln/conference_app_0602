from conferences.views import ConferenceListView, ConferenceDetailView
from django.urls import path

urlpatterns = [
    # visi views kurie yra ne funkcija, o klases
    # juos kvieciam su papildoma as_view
    path("", ConferenceListView.as_view()),
    path("<int:pk>/", ConferenceDetailView.as_view(), name = "conference_detail"),

]