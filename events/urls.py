from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventsList.as_view(), name='home'),
    path("<int:event_id>", views.event_detail, name="event_detail"),
    path('<int:event_id>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<int:event_id>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
]
