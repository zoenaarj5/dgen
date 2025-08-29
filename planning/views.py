from collections import defaultdict
from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from django.db import transaction
from planning.forms import EventCreationForm, EventEditForm
from .models import Event
from django.utils import timezone
import calendar

def get_month_calendar(year,month):
    calen = calendar.Calendar(firstweekday=0)
    monthdays = calen.monthdatescalendar(year,month)
    return monthdays

def home(request):
    title="Évènements"
    now=timezone.now()
    events = Event.objects.exclude(start_date__lt=now).order_by("-start_date")
    context = {
        "title":title,
        "events":events
    }
    return render(request,"planning/home.html",context)

def calendarView(request,year=None,month=None):
    today = date.today()
    if not year:
        year = today.year
    if not month:
        month = today.month
    year, month = int(year), int(month)
    (prevMonthYear, prevMonthMonth) = (year-1, 12) if month==1 else (year, month-1)
    (nextMonthYear, nextMonthMonth) = (year+1, 1) if month==12 else (year, month+1)
    (prevYearYear, prevYearMonth) = (year-1, month)
    (nextYearYear, nextYearMonth) = (year+1, month)
    events = Event.objects.filter(start_date__year=year,start_date__month = month)
    title="Calendrier"
    dayNames = "Lun Mar Mer Jeu Ven Sam Dim"
    monthNames = "Janvier Février Mars Avril Mai Juin Juillet Août Septembre Octobre Novembre Décembre"
    eventsByDay = defaultdict(list)
    for event in events:
        # Using start date in date format instead of date format
        startDate=date(event.start_date.year,event.start_date.month,event.start_date.day)
        eventsByDay [startDate].append(event)

    monthDays = get_month_calendar(year,month)
    
    context={
        "title":title,
        "month_days":monthDays,
        "events_by_day":eventsByDay,
        "year":year,
        "month":month,
        "day_names":dayNames,
        "month_name":monthNames.split()[month-1],
        "events":events,
        "prevMonthYear":prevMonthYear,
        "prevMonthMonth":prevMonthMonth,
        "nextMonthYear":nextMonthYear,
        "nextMonthMonth":nextMonthMonth,
        "prevYearYear":prevYearYear,
        "prevYearMonth":prevYearMonth,
        "nextYearYear":nextYearYear,
        "nextYearMonth":nextYearMonth,
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
        event_form = EventEditForm(request.POST,instance=event)
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
