from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.event_name


class Ticket(models.Model):
    ticket_holder = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_tickets"
    )
    date_issued = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="event_tickets"
    )

    def __str__(self):
        return f"Ticket for {self.ticket_holder}"


class Review(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="event_reviews"
    )
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_reviewers")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Review of event '{self.event}' by {self.reviewer}"
