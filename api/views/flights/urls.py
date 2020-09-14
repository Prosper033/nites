from django.urls import path
from api.views.flights import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:flight_id>/', views.details, name="details"),
    path('<int:flight_id>/edit', views.edit, name="edit"),
    path('<int:flight_id>/delete', views.delete, name="delete"),
    path('create', views.create, name="create"),
    path('search', views.search_flight, name="search_flight")
]
