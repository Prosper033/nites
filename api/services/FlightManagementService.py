from abc import ABCMeta, abstractmethod
from typing import List, Callable
from datetime import date

from api.dto.FlightDto import CreateFlightDto, EditFlightDto, ListFlightDto, FlightDetailsDto, SearchFlightDetailsDto
from api.dto.CommonDto import SelectOptionDto
from api.repositories.FlightRepository import FlightRepository


class FlightManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create(self, model: CreateFlightDto):
        """Creates a flight object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditFlightDto):
        """Updates a flight object"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, flight_id: int):
        """Deletes a flight object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListFlightDto]:
        """Gets a list of flights"""
        raise NotImplementedError

    @abstractmethod
    def get(self, flight_id: int) -> FlightDetailsDto:
        """Gets a single flight"""
        raise NotImplementedError

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Creates a flight object"""
        raise NotImplementedError

    def search_related_flight(self, take_off_point: str, take_off_time: date, destination: str)-> SearchFlightDetailsDto:
        """Returns Flight"""
        raise NotImplementedError


class DefaultFlightManagementService(FlightManagementService):
    repository: FlightRepository = None

    def __init__(self, repository: FlightRepository):
        self.repository = repository

    def create(self, model: CreateFlightDto):
        return self.repository.create(model)

    def edit(self, id: int, model: EditFlightDto):
        return self.repository.edit(id, model)

    def delete(self, flight_id: int):
        return self.repository.delete(flight_id)

    def list(self) -> List[ListFlightDto]:
        return self.repository.list()

    def get(self, flight_id: int) -> FlightDetailsDto:
        return self.repository.get(flight_id)

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()

    def search_related_flight(self, take_off_point: str, take_off_time: date, destination: str) -> SearchFlightDetailsDto:
        return self.repository.search_related_flight(take_off_point, take_off_time, destination)
