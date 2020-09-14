from abc import ABCMeta, abstractmethod
from typing import List

from api.dto.BookingDto import CreateBookingDto, EditBookingDto, GetBookingDto, ListBookingDto
from api.repositories.BookingRepository import BookingRepository


class BookingManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_booking(self, model: CreateBookingDto):
        """Create a Booking Object"""
        raise NotImplementedError

    @abstractmethod
    def list_bookings(self) -> List[ListBookingDto]:
        """List Booking Objects"""
        raise NotImplementedError

    @abstractmethod
    def edit_booking(self, id:int, model: EditBookingDto):
        """Edit a Booking Object"""
        raise NotImplementedError

    @abstractmethod
    def get_booking(self, id:int) -> GetBookingDto:
        """Get a Booking Object"""
        raise NotImplementedError

    def delete_booking(self, id:int):
        """Delete Booking Object"""
        raise NotImplementedError


class DefaultBookingManagementService(BookingManagementService):
    repository: BookingRepository

    def __init__(self,  repository: BookingRepository):
        self.repository = repository

    def create_booking(self, model: CreateBookingDto):
        return self.repository.create_booking(model)

    def list_bookings(self) -> List[ListBookingDto]:
        return self.repository.list_bookings()

    def edit_booking(self, id:int, model: EditBookingDto):
        return self.repository.edit_booking(id, model)

    def delete_booking(self, id:int):
        return self.repository.delete_booking(id)

    def get_booking(self, id: int) -> GetBookingDto:
        return self.repository.get_booking(id)

