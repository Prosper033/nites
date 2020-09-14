from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect
from datetime import date
from api.dto.FlightDto import FlightDetailsDto, ListFlightDto, EditFlightDto, CreateFlightDto, SearchFlightDetailsDto
from api.service_provider import api_service_container
from api.models import Flight


def index(request):
    flights = api_service_container.flight_management_service().list()
    context = {
        "title": "Flights",
        "flights": flights  # list flight dto
    }
    return render(request, 'api/Flight/index.html', context)


def details(request, flight_id):
    flight = __get_flight_details_dto_or_rise_404(flight_id)
    context = {
        "title": f"flight {flight.flight_number}",
        "flight": flight
    }
    return render(request, "api/Flight/view.html", context)


def __get_flight_details_dto_or_rise_404(flight_id) -> FlightDetailsDto:
    try:
        flight = api_service_container.flight_management_service().get(flight_id=flight_id)
    except Flight.DoesNotExist:
        raise Http404("requested flight dose not exit")
    return flight


def __get_create_flight_dto_from_request(request: HttpRequest) -> CreateFlightDto:
    create_flight_dto = CreateFlightDto()
    create_flight_dto.flight_number = request.POST["flightNumber"]
    __set_flight_attributes_from_request(create_flight_dto, request)
    return create_flight_dto


def __get_edit_flight_dto_from_request(flight_id: int, request: HttpRequest) -> EditFlightDto:
    edit_flight_dto = EditFlightDto()
    edit_flight_dto.id = flight_id
    __set_flight_attributes_from_request(edit_flight_dto, request)
    return edit_flight_dto


def __set_flight_attributes_from_request(edit_flight_dto, request):
    edit_flight_dto.take_off_point = request.POST["take_off_point"]
    edit_flight_dto.take_off_time = request.POST["take_off_time"]
    edit_flight_dto.destination = request.POST["destination"]
    edit_flight_dto.price = request.POST["price"]
    edit_flight_dto.aircraft_id = int(request.POST["aircraftId"])
    edit_flight_dto.flight_class = request.POST["flight_class"]


def __get_flight_details_dto_or_raise_404(flight_id) -> FlightDetailsDto:
    try:
        flight = api_service_container.flight_management_service().get(flight_id)
    except Flight.DoesNotExist:
        raise Http404("The requested flight does not exist")
    return flight


def edit(request, flight_id):
    flight_details_dto = __get_flight_details_dto_or_raise_404(flight_id)
    aircraft = api_service_container.aircraft_management_service().get_all_for_select_list()
    context = {
        "title": f"Edit Flight {flight_details_dto.flight_number}",
        "flight_id": flight_id,
        "flight": flight_details_dto,
        "take_off_time": flight_details_dto.take_off_time.strftime("%Y-%m-%d %H:%M:%S"),
        "aircraft": aircraft
    }
    new_flight_details_dto = __edit_if_post_method(context, flight_id, request)
    if new_flight_details_dto is not None:
        context["flight"] = new_flight_details_dto
    return render(request, "api/Flight/edit.html", context)


def create(request):
    aircraft = api_service_container.aircraft_management_service().get_all_for_select_list()
    context = {
        "aircraft": aircraft
    }
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect("index")
    return render(request, "api/Flight/create.html", context)


def delete(request, flight_id: int):
    try:
        api_service_container.flight_management_service().delete(flight_id)
        return redirect("index")
    except Exception:
        raise Http404("No such flight exists")


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            flight = __get_create_flight_dto_from_request(request)
            api_service_container.flight_management_service().create(flight)
            context["saved"] = True
        except Exception as e:
            print(e)
            context["saved"] = False


def __edit_if_post_method(context, flight_id: int, request: HttpRequest) -> FlightDetailsDto:
    if request.method == "POST":
        try:
            flight = __get_edit_flight_dto_from_request(flight_id, request)
            api_service_container.flight_management_service().edit(flight_id, flight)
            context["saved"] = True
            return __get_flight_details_dto_or_raise_404(flight_id)
        except Exception as e:
            print(e)
            context["saved"] = False


def search_flight(request) -> SearchFlightDetailsDto:
    flights = api_service_container.flight_management_service() \
        .search_related_flight(request.GET.get("take_off_point", None), request.GET["take_off_time"],
                               request.GET["destination"])
    context = {
        "flights": flights,
        "take_off_point": request.GET["take_off_point"],
        "take_off_time": request.GET["take_off_time"],
        "destination": request.GET["destination"]
    }
    return render(request, 'api/Flight/searchflight.html', context)
