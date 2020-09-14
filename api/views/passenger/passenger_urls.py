from django.urls import path
from api.views.passenger import passenger_views

urlpatterns = [
   path('', passenger_views.index_passenger, name='index_passenger'),
   path('create', passenger_views.create_passenger, name='crete_passenger'),
   path('<name>/', passenger_views.details_passenger, name="details_passenger"),
   path('<name>/edit', passenger_views.edit_passenger, name="edit_passenger"),
   path('<name>/delete', passenger_views.delete_passenger, name='delete_passenger')
]