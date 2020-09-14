from django.urls import path
from api.views.booking import booking_views

urlpatterns = [
    path('', booking_views.index_booking, name='index_booking'),
    path('create', booking_views.create_booking, name='create_booking'),
    path("<id>/", booking_views.details_booking, name='details_booking'),
    path("<id>/edit", booking_views.edit_booking, name='edit_booking'),
    path("<id>/delete", booking_views.delete_booking, name="delete_booking")
]