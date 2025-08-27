from django.shortcuts import get_object_or_404, redirect, render
from django.db import transaction
from planning.forms import EventCreationForm
from .models import Event
from django.utils import timezone

def home(request):
    title="Évènements"
    now=timezone.now()
    events = Event.objects.exclude(start_date__lt=now).order_by("-start_date")
    context = {
        "title":title,
        "events":events
    }
    return render(request,"planning/home.html",context)

def calendar(request):
    title="Calendrier"
    context={
        "title":title
    }
    return render(request,"planning/calendar.html",context)

def events(request,from_latest):
    desc=False if from_latest==0 else True
    events=Event.objects.order_by("-start_date") if desc else Event.objects.order_by("start_date")
    title="Évènements"
    context={
        "title":title,
        "events":events
    }
    return render(request,"planning/events.html",context)

def eventDetail(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    title="Détail évènement"
    context = {
        "title":title,
        "event":event
    }
    return render(request,"planning/event-detail.html",context)

def addEvent(request):
    if request.method=="POST":
        event_form = EventCreationForm(request.POST)
        if(event_form.is_valid()):
            with transaction.atomic():
                event = event_form.save()
                event.save()
                return redirect(f"/planning/event-detail/{event.id}")
    else:
        event_form=EventCreationForm()

    context = {
        "title":"Nouvel évènement",
        "event_form":event_form
    }

    return render(request, "planning/add-event.html",context)

def editEvent(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    if request.method=="POST":
        event_form = EventCreationForm(request.POST,instance=event)
        if(event_form.is_valid()):
            with transaction.atomic():
                event = event_form.save()
                event.save()
                return redirect(f"/planning/event-detail/{event.id}")
    else:
        event_form=EventCreationForm(instance=event)
    context ={
        "title":f"Modifier l'événement \"{event.title}\"",
        "event_form":event_form
    }
    return render(request, "planning/edit-event.html",context)
