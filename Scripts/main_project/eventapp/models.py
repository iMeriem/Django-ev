from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime
from django import forms

# Create your models here.
	
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    venue = models.CharField(max_length=100)
    seats = models.IntegerField()
    amount = models.DecimalField(
        max_digits=11,
        decimal_places=2
    )
    date = models.DateTimeField()
	
    duration = models.CharField(max_length=100,
	 help_text='e.g. 3 hours, 5 days'
	)
		
	
def __str__(self):
        return self.name
		

class Date(models.Model):
    event_start = models.DateTimeField()
    event_end= models.DateTimeField()
class Ticket_Class(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    type= models.CharField(max_length=20)

class EventTicketSell(models.Model):
    event= models.ForeignKey(Event)
    date= models.ForeignKey(Date)
    ticket= models.ForeignKey(Ticket_Class)
    max_sellable_tickets= models.IntegerField()
	
