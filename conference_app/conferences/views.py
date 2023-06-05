from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Conference

# Create your views here.

class ConferenceListView (ListView):
    model = Conference

class ConferenceDetailView(DetailView):
    model = Conference

#Alternatyva DetailView
# def conference_detail(request, pk): #pk ateina is urls failo: path("<int:pk>")
#     conference = get_object_or_404(Conference, pk = pk)
#     return render(request, "conferences/conference_detail.html", {"object": conference})

