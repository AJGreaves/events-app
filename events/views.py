from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event, Ticket, Review
from .forms import ReviewForm

# Create your views here.


class EventsList(generic.ListView):

    model = Event
    template_name = "index.html"
    paginate_by = 12


def event_detail(request, event_id, *args, **kwargs):

    queryset = Event.objects.all()
    event = get_object_or_404(queryset, pk=event_id)
    reviews = Review.objects.filter(event=event).order_by("-created_on")
    review_form = ReviewForm()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer = request.user
            review.event = event
            review.save()
        else:
            review_form = ReviewForm()
    else:
        review_form = ReviewForm()

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "review_form": review_form,
            "reviews": reviews
        }
    )


def review_edit(request, event_id, review_id, *args, **kwargs):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=event_id)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.reviewer == request.user:
            review = review_form.save(commit=False)
            review.reviewer = request.user
            review.event = event
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating Review!')

    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))


def review_delete(request, event_id, review_id, *args, **kwargs):
    """
    view to delete review
    """
    queryset = Event.objects.all()
    event = get_object_or_404(queryset, pk=event_id)
    review = get_object_or_404(Review, pk=review_id)

    if review.reviewer == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))
