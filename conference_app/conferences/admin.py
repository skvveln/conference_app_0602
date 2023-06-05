from django.contrib import admin
from conferences.models import Conference
from events.models import Event

# klase nurodanti, kokie dar susije modeliai turetu buti
class EventInline(admin.TabularInline):
    model = Event

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date']
    inlines = [EventInline]

admin.site.register(Conference, ConferenceAdmin)