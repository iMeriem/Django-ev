from django.shortcuts import render
from django.http import HttpResponse
from .models import Event



# Create your views here.
def list(request):
   event_list = Event.objects.all();
   return render(request, 'events/list.html', {'event_list': event_list})
def home(request):
     return render('home.html')
