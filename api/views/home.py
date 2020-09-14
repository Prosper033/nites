from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect

from api.dto.BookingDto import CreateBookingDto, EditBookingDto, GetBookingDto, ListBookingDto
from api.models import Booking
from api.service_provider import api_service_container


def index(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'index.html', context)
