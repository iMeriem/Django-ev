from django.contrib import admin
from .models import Event,Date,Ticket_Class,EventTicketSell

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'date')
    search_fields = ('title', )
	

admin.site.register(Event, EventAdmin)
admin.site.register(Date)
admin.site.register(Ticket_Class)
admin.site.register(EventTicketSell)

