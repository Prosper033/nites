from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('second_view', views.second_view, name="second_view"),
    path('flights', views.list_flights, name="list_flights"),
    path('flights/<int:flight_id>', views.view_flight, name="view_flight")
]
