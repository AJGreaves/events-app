from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event, Ticket

# Create your views here.


class EventsList(generic.ListView):
    """
    This is Django's generic ListView. We are a little limited as to
    what we can do with this, but if we really needed to, we could
    access the request object here too.

    It's a class, which is why we had used class-based views in the
    original blog material. Now, to show what's going on under the
    hood, so to speak, we'll use function-based ones instead.
    """

    model = Event
    template_name = "index.html"
    paginate_by = 12


def event_detail(request, event_id, *args, **kwargs):

    event = get_object_or_404(Event, pk=event_id)

    return render(
        request,
        "events/event_ticket_list.html",
        {"event": event}
    )
