from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event, Ticket

# Create your views here.


class EventsList(generic.ListView):

    model = Event
    template_name = "index.html"
    paginate_by = 12


def event_detail(request, event_id, *args, **kwargs):

    queryset = Event.objects.filter()
    event = get_object_or_404(queryset, pk=event_id)

    return render(
        request,
        "events/event_detail.html",
        {"event": event}
    )
