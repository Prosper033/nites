from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect

from api.dto.BookingDto import CreateBookingDto, EditBookingDto, GetBookingDto, ListBookingDto
from api.models import Booking
from api.service_provider import api_service_container


def index_booking(request):
    bookings = api_service_container.booking_management_service().list_bookings()
    context = {
        'title': 'Booking',
        'bookings': bookings
    }
    return render(request, 'api/Bookings/indexBooking.html', context)


def details_booking(request, id:int):
    booking = __get_booking_dto_or_rise_404(id)
    context = {
        "title": f"Booking{booking.booking_reference}",
        "booking": booking
    }
    return render(request, "api/Bookings/detailsBooking.html", context)


def create_booking(request):
    flight = api_service_container.flight_management_service().get_all_for_select_list()
    passenger = api_service_container.passenger_management_service().get_all_for_select_list()
    context={
        "flight": flight,
        "passenger": passenger
    }
    __create_if_method_post(context, request)
    if request.method == "POST" and context["saved"]:
        redirect("index_booking")
    return render(request, 'api/Bookings/createBooking.html', context)


def __create_booking_dto_form_request(request: HttpRequest) -> CreateBookingDto:
    create_booking_dto = CreateBookingDto()
    create_booking_dto.booking_reference = request.POST["booking_reference"]
    __set_booking_attribute_from_request(create_booking_dto,  request)
    return create_booking_dto


def __create_if_method_post(context, request):
    if request.method == "POST":
        try:
            booking = __create_booking_dto_form_request(request)
            api_service_container.booking_management_service().create_booking(booking)
            context["saved"] = True
        except Exception as e:
            print(e)
            context["saved"] = False


def __set_booking_attribute_from_request(edit_booking_dto, request):
    edit_booking_dto.booking_reference = request.POST["booking_reference"]
    edit_booking_dto.flight_id = int(request.POST["flight_id"])
    edit_booking_dto.destination = request.POST["destination"]
    edit_booking_dto.take_off_point = request.POST["take_off_point"]
    edit_booking_dto.take_off_time = request.POST["take_off_time"]
    edit_booking_dto.price = request.POST["price"]
    edit_booking_dto.flight_class = request.POST["flight_class"]


def __get_booking_dto_or_rise_404(id) -> GetBookingDto:
    try:
        booking = api_service_container.booking_management_service().get_booking(id)
    except Booking.DoesNotExist:
        raise Http404('Tried Booking dose not exit')
    return booking


def edit_booking(request, id):
    booking_details_dto = __get_booking_dto_or_rise_404(id=id)
    flight = api_service_container.flight_management_service().get_all_for_select_list()
    context = {
        "flight": flight,
        "booking": booking_details_dto,
        "title": f"Edit: booking{booking_details_dto.booking_reference}",
        "take_off_time": booking_details_dto.take_off_time.strftime("%Y-%m-%d %H:%M:%S"),
        "id": id
    }
    new_booking_details_dto = __edit_if_method_is_post(context, id, request)
    if new_booking_details_dto is not None:
        context["booking"] = new_booking_details_dto
    return render(request, "api/Bookings/editBooking.html", context)


def delete_booking(_, id: int):
    try:
        api_service_container.booking_management_service().delete_booking(id)
        return redirect('index_booking')
    except Exception:
        raise Http404("Booking dose not exit")


def __get_edit_booking_dto_from_request(id: int, request: HttpRequest):
    edit_booking_dto = EditBookingDto()
    edit_booking_dto.id = id
    __set_booking_attribute_from_request(edit_booking_dto, request)
    return edit_booking_dto


def __edit_if_method_is_post(context, id: int, request):
    if request.method == "POST":
        try:
            booking = __get_edit_booking_dto_from_request(id, request)
            api_service_container.booking_management_service().edit_booking(id, booking)
            context["saved"] = True
            return __get_booking_dto_or_rise_404(id)
        except Exception as e:
            print(e)
            context['saved'] = False




