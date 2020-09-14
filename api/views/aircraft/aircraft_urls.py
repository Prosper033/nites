from django.urls import path
from api.views.aircraft import aircraft_views

urlpatterns = [
    path('', aircraft_views.index_aircraft, name="index_aircraft"),
    path('create', aircraft_views.create_aircraft, name="create_aircraft"),
    path('<aircraft_id>/', aircraft_views.details_aircraft, name='details_aircraft'),
    path('<aircraft_id>/edit', aircraft_views.edit_aircraft, name='edit_aircraft'),
    path('<aircraft_id>/delete', aircraft_views.delete_aircraft, name='delete_aircraft'),
    path('_login', aircraft_views.login_get, name='login'),
    path('log', aircraft_views.login_post, name="login post")
]

