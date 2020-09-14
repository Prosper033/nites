from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.decorators.http import require_GET, require_POST

from api.dto.AircraftDto import AircraftDetailsDto, CreateAircraftDto, ListAircraftDto, EditAircraftDto
from api.models import Aircraft
from api.service_provider import api_service_container


def index_aircraft(request):
    aircrafts = api_service_container.aircraft_management_service().list()
    context = {
        "title": "Aircraft",
        "aircrafts": aircrafts
    }
    return render(request, 'api/Aircraft/indexAircraft.html', context)


def create_aircraft(request):
    context = dict()
    __create_if_post_method(context, request)
    if request.method == "POST" and context["saved"]:
        return redirect('index_aircraft')
    return render(request, 'api/Aircraft/createAircraft.html', context)


def details_aircraft(request, aircraft_id):
    aircraft = __get_aircraft_details_dto_or_rise_404(aircraft_id)
    context = {
        'title': f" Aircraft {aircraft.aircraft_number}",
        'aircraft': aircraft,

    }
    return render(request, 'api/Aircraft/detailsAircraft.html', context)


def __get_aircraft_details_dto_or_rise_404(aircraft_id) -> AircraftDetailsDto:
    try:
        aircraft = api_service_container.aircraft_management_service().get(aircraft_id=aircraft_id)
    except Aircraft.DoesNotExist:
        raise Http404('Aircraft dose not exit')
    return aircraft


def __set_aircraft_attribute_from_request(edit_aircraft_dto, request):
    edit_aircraft_dto.aircraft_number = request.POST["aircraft_number"]
    edit_aircraft_dto.name = request.POST["name"]
    edit_aircraft_dto.type = request.POST["type"]
    edit_aircraft_dto.capacity = int(request.POST["capacity"])


def __get_aircraft_dto_from_request(request: HttpRequest) -> CreateAircraftDto:
    create_aircraft_dto = CreateAircraftDto()
    create_aircraft_dto.aircraft_number = request.POST["aircraft_number"]
    __set_aircraft_attribute_from_request(create_aircraft_dto, request)
    return create_aircraft_dto


def __create_if_post_method(context, request):
    if request.method == "POST":
        try:
            aircraft = __get_aircraft_dto_from_request(request)
            api_service_container.aircraft_management_service().create(aircraft)
            context["saved"] = True
        except Exception as e:
            print(e)
            context["saved"] = False


def __get_edit_flight_dto_from_request(aircraft_id: int, request: HttpRequest) -> EditAircraftDto:
    edit_aircraft_dto = EditAircraftDto()
    edit_aircraft_dto.id = aircraft_id
    __set_aircraft_attribute_from_request(edit_aircraft_dto, request)
    return edit_aircraft_dto


def __edit_if_post_method(context, aircraft_id: id, request):
    if request.method == "POST":
        try:
            aircraft = __get_edit_flight_dto_from_request(aircraft_id, request)
            api_service_container.aircraft_management_service().edit(aircraft_id, aircraft)
            context["saved"] = True
            return __get_aircraft_details_dto_or_rise_404(aircraft_id)
        except Exception as e:
            print(e)
            context["saved"] = False


def edit_aircraft(request, aircraft_id):
    aircraft_details_dto = __get_aircraft_details_dto_or_rise_404(aircraft_id)
    context = {
        'title': f"Edit aircraft{aircraft_details_dto.aircraft_number}",
        'aircraft': aircraft_details_dto
    }
    new_aircraft_details_dto = __edit_if_post_method(context, aircraft_id, request)
    if new_aircraft_details_dto is not None:
        context["aircraft"] = new_aircraft_details_dto

    return render(request, 'api/Aircraft/editAircraft.html', context)


def delete_aircraft(request, aircraft_id: int):
    try:
        api_service_container.aircraft_management_service().delete(aircraft_id)
        return redirect('index_aircraft')
    except Exception:
        raise Http404('aircraft dose not exit')


@require_GET
def login_get(request):
    context = {
        "title": 'login'
    }
    return render(request, 'api/Aircraft/login.html', context)


@require_POST
def login_post(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is None:
        return login_get(request)
    login(request, user)
    request.session['user_id'] = user.id
    return redirect('index_aircraft')
