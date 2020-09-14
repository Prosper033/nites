from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect

from api.dto.PassengerDto import ListPassengerDto, EditPassengerDto, CreatePassengerDto, PassengerDetailsDto
from api.models import Passenger
from api.service_provider import api_service_container


def index_passenger(request):
    passengers = api_service_container.passenger_management_service().list_passenger()
    context = {
        'title': "Passenger",
        'passengers': passengers
    }
    return render(request, 'api/passenger/indexPassenger.html', context)


def details_passenger(request, name):
    passenger = __get_passenger_details_dto_or_rise_404(name)
    context = {
        'title': f" Passenger {passenger.name}",
        'passenger': passenger
    }
    return render(request, 'api/passenger/passengerDetails.html', context)


def __get_passenger_details_dto_or_rise_404(name) -> PassengerDetailsDto:
    try:
        passenger = api_service_container.passenger_management_service().passenger_details(name=name)
    except Passenger.DoesNotExist:
        raise Http404('Passenger dose not exit')
    return passenger


def __set_passenger_attribute_from_request(edit_passenger_dto, request):
    edit_passenger_dto.name = request.POST["name"]
    edit_passenger_dto.phone = request.POST["phone"]
    edit_passenger_dto.email = request.POST["email"]
    edit_passenger_dto.address = request.POST["address"]


def __get_passenger_dto_from_request(request: HttpRequest) -> CreatePassengerDto:
    create_passenger_dto = CreatePassengerDto()
    create_passenger_dto.name = request.POST["name"]
    __set_passenger_attribute_from_request(create_passenger_dto, request)
    return create_passenger_dto


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            passenger = __get_passenger_dto_from_request(request)
            api_service_container.passenger_management_service().create_passenger(passenger)
            context["saved"] = True
        except Exception as e:
            print(e)
            context["saved"] = False


def __get_edit_passenger_dto_from_request(name: str, request: HttpRequest) -> EditPassengerDto:
    edit_passenger_dto = EditPassengerDto()
    edit_passenger_dto.name = name
    __set_passenger_attribute_from_request(edit_passenger_dto, request)
    return edit_passenger_dto


def __edit_if_post_method(context, name: str, request):
    if request.method == "POST":
        try:
            passenger = __get_edit_passenger_dto_from_request(name, request)
            api_service_container.passenger_management_service().edit_passenger(name, passenger)
            context["saved"] = True
            return __get_passenger_details_dto_or_rise_404(name)
        except Exception as e:
            print(e)
            context["saved"] = False


def create_passenger(request):
    context = dict()
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect('index_passenger')
    return render(request, 'api/passenger/createPassenger.html', context)


def delete_passenger(request, name: str):
    try:
        api_service_container.passenger_management_service().delete_passenger(name)
        return redirect('index_passenger')
    except Exception:
        raise Http404('Passenger dose not exit')


def edit_passenger(request, name: str):
    passenger_details_dto = __get_passenger_details_dto_or_rise_404(name)
    context = {
        'title': f"Edit passenger{passenger_details_dto.name}",
        'passenger': passenger_details_dto
    }
    new_passenger_details_dto = __edit_if_post_method(context, name, request)
    if new_passenger_details_dto is not None:
        context["passenger"] = new_passenger_details_dto

    return render(request, 'api/passenger/editPassenger.html', context)