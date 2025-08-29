from django.urls import path

from . import views
urlpatterns = [
    path("",views.home,name="planning-home"),
    path("add-event/",views.addEvent,name="addEvent"),
    path("edit-event/<int:event_id>",views.editEvent,name="editEvent"),
    path("event-detail/<int:event_id>",views.eventDetail,name="eventDetail"),
    path("events/<int:from_latest>",views.events,name="events"),
    path("calendar/",views.calendarView,name="calendar"),
    path("calendar/<int:year>/<int:month>",views.calendarView,name="calendarMonth")
]