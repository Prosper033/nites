from abc import ABCMeta, abstractmethod
from typing import List

from api.dto.BookingDto import CreateBookingDto, EditBookingDto, GetBookingDto, ListBookingDto
from api.models import Booking


class BookingRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_booking(self, model: CreateBookingDto):
        """Create a Booking Object"""
        raise NotImplementedError

    @abstractmethod
    def list_bookings(self) -> List[ListBookingDto]:
        """List Booking Objects"""
        raise NotImplementedError

    @abstractmethod
    def edit_booking(self, id: int, model: EditBookingDto):
        """Edit a Booking Object"""
        raise NotImplementedError

    @abstractmethod
    def get_booking(self, id: int) -> GetBookingDto:
        """Get a Booking Object"""
        raise NotImplementedError

    def delete_booking(self, id: int):
        """Delete Booking Object"""
        raise NotImplementedError


class DjangoORMBookingRepository(BookingRepository):
    def create_booking(self, model: CreateBookingDto):
        booking = Booking()
        booking.booking_reference = model.booking_reference
        booking.flight_id = model.flight_id
        booking.take_off_point = model.take_off_point
        booking.price = model.price
        booking.take_off_time = model.take_off_time
        booking.destination = model.destination
        booking.flight_class = model.flight_class
        booking.name = model.name
        booking.phone = model.phone
        booking.email = model.email
        booking.address = model.address
        booking.save()

    def edit_booking(self, id: int, model: EditBookingDto):
        try:
            booking = Booking.objects.get(id=id)
            booking.flight_id = model.flight_id
            booking.destination = model.destination
            booking.take_off_time = model.take_off_time
            booking.take_off_point = model.take_off_point
            booking.price = model.price
            booking.flight_class = model.flight_class
            booking.name = model.name
            booking.phone = model.phone
            booking.email = model.email
            booking.address = model.address
            booking.save()
        except Booking.DoesNotExist as e:
            message = "Tried Booking dost Not exit"
            print(message)
            raise e

    def list_bookings(self) -> List[ListBookingDto]:
        bookings = list(Booking.objects.values("id",
                                               "destination",
                                               "price",
                                               "take_off_time",
                                               "take_off_point",
                                               "flight_class",
                                               "flight__flight_number",
                                               "booking_reference"
                                               ))
        result: List[ListBookingDto] = []
        for booking in bookings:
            item = ListBookingDto()
            item.id = booking['id']
            item.destination = booking["destination"]
            item.price = booking["price"]
            item.take_off_time = booking["take_off_time"]
            item.take_off_point = booking["take_off_point"]
            item.flight_class = booking["flight_class"]
            item.flight_number = booking["flight__flight_number"]
            item.booking_reference = booking["booking_reference"]
            result.append(item)
        return result

    def get_booking(self, id: int) -> GetBookingDto:
        try:
            booking = Booking.objects.get(id=id)
            result = GetBookingDto()
            result.flight_number = booking.flight.flight_number
            result.destination = booking.destination
            result.booking_reference = booking.booking_reference
            result.take_off_time = booking.take_off_time
            result.take_off_point = booking.take_off_point
            result.price = booking.price
            result.flight_class = booking.flight_class
            result.name = booking.name
            result.phone = booking.phone
            result.email = booking.email
            result.address = booking.address
            return result
        except Booking.DoesNotExist as e:
            message = "Tried Booking dost Not exit"
            print(message)
            raise e

    def delete_booking(self, id: int):
        try:
            Booking.objects.filter(id=id).delete()
        except Booking.DoesNotExist as e:
            message = "Tried Booking dost Not exit"
            print(message)
            raise e

