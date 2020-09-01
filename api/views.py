from django.http import HttpResponse
from.models import Flight
from django.urls import reverse

# Create your views here.


def index(request):
    return HttpResponse('it works')


def second_view(request):
    return HttpResponse('this is the second view')


def list_flights(request):
    flights = list(Flight.objects.select_related().all())
    print(flights)
    return HttpResponse(__get_flight_template(flights), content_type="text/html")


def view_flight(request, flight_id):
    flight = Flight.objects.select_related().get(id=flight_id)
    return HttpResponse(__get_display_flight_template(flight), content_type="text/html")


def __get_flight_template(flight):
    return f'''
    <!doctype HTML>
    <html>
        <head>
             <title> List of Flight</title>
        </head>
        <body>
            <table border= 1>
                <thead>
                        <tr>
                            <th>Aircraft Number</th>
                            <th>Flight Number</th>
                            <th>take_off_point</th>
                            <th>take_off_time</th>
                            <th>destination</th>
                            <th>price</th>
                            <th>flight_class</th>
                        </tr>
                </thead>
                <tbody>
                    {str.join('',[__get_flight_row(f) for f in flight])}
                </tbody>
        </body>
</html>
'''


def __get_flight_row(flight: Flight):
    return f'''
<tr>
    <td>{flight.aircraft.aircraft_number}</td>
    <td>{flight.flight_number}</td>
    <td>{flight.take_off_point}</td>
    <td>{flight.take_off_time}</td>
    <td>{flight.destination}</td>
    <td>{flight.price}</td>
    <td>{flight.flight_class}</td>
    <td><a href="{reverse("view_flight", kwargs={'flight_id': flight.id})}">View details</a></td>
</tr>'''


def __get_display_flight_template(flight: Flight):
    return f'''<!doctype html>
<html>
    <head>
        <title>Flight (flight {flight.flight_number} - Flights = Airline Management System</title>
    </head>
    <body>
        <div>
            <h3>Flight details:{flight.flight_number}</h3>
        </div>
        <div>
            <label>Flight Number:</label>
            <label>{flight.flight_number}</label>
        </div>
        <div>
            <label>Aircraft Number:</label>
            <label>{flight.aircraft.aircraft_number}</label>
        </div>
        <div>
            <label>Take off point:</label>
            <label>{flight.take_off_point}</label>
        </div>
        <div>
            <label>Take off time:</label>
            <label>{flight.take_off_time}</label>
        </div>
        <div>
            <label>Destination:</label>
            <label>{flight.destination}</label>
        </div>
        <div>
            <label>price:</label>
            <label>{flight.price}</label>
        </div>
        <div>
            <label>flight class:</label>
            <label>{flight.flight_class}</label>
        </div>
    </body>
</html>
        
        

'''

