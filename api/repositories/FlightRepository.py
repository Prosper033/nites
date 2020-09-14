from abc import ABCMeta, abstractmethod
from typing import List
from datetime import date
from api.dto.FlightDto import CreateFlightDto, EditFlightDto, FlightDetailsDto, ListFlightDto, SearchFlightDetailsDto
from api.dto.CommonDto import SelectOptionDto
from api.models import Flight


class FlightRepository(metaclass=ABCMeta):
    @abstractmethod
    def create(self, model: CreateFlightDto):
        """Create a Flight Object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditFlightDto):
        """Edit a flight object"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, flight_id: int):
        """Delete a flight object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListFlightDto]:
        """Get List of Flight"""
        raise NotImplementedError

    @abstractmethod
    def get(self, flight_id: int) -> FlightDetailsDto:
        """A flight detail"""
        raise NotImplementedError

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Creates a flight object"""
        raise NotImplementedError

    def search_related_flight(self, take_off_point: str, take_off_time: date,
                              destination: str) -> SearchFlightDetailsDto:
        """Returns Flight"""
        raise NotImplementedError


class DjangoORMFlightRepository(FlightRepository):
    def create(self, model: CreateFlightDto):
        flight = Flight()
        flight.price = model.price
        flight.flight_class = model.flight_class
        flight.take_off_time = model.take_off_time
        flight.flight_number = model.flight_number
        flight.aircraft_id = model.aircraft_id
        flight.take_off_point = model.take_off_point
        flight.destination = model.destination
        flight.save()

    def edit(self, id: int, model: EditFlightDto):
        try:
            flight = Flight.objects.get(id=id)
            flight.price = model.price
            flight.flight_class = model.flight_class
            flight.take_off_time = model.take_off_time
            flight.aircraft_id = model.aircraft_id
            flight.take_off_point = model.take_off_point
            flight.destination = model.destination
            flight.save()
        except Flight.DoesNotExist as e:
            message = "Tried to update a flight that dose not exit"
            print(message)
            raise e

    def delete(self, flight_id: int):
        try:
            flight = Flight.objects.get(id=flight_id)
            flight.delete()
        except Flight.DoesNotExist as e:
            message = "Tried to delete a flight that dose not exit"
            print(message)
            raise e

    def get(self, flight_id: int) -> FlightDetailsDto:
        try:
            flight = Flight.objects.select_related("aircraft").get(id=flight_id)
            result = FlightDetailsDto()
            result.id = flight.id
            result.flight_number = flight.flight_number
            result.take_off_point = flight.take_off_point
            result.take_off_time = flight.take_off_time
            result.destination = flight.destination
            result.price = flight.price
            result.flight_class = flight.flight_class
            result.aircraft_number = flight.aircraft.aircraft_number
            return result
        except Flight.DoesNotExist as e:
            message = "Tried flight dose not exit"
            print(message)
            raise e

    def list(self) -> List[ListFlightDto]:
        flights = list(Flight.objects.values("id",
                                             "flight_number",
                                             "aircraft__aircraft_number",
                                             "take_off_point",
                                             "destination",
                                             "price",
                                             "flight_class"))

        result: List[ListFlightDto] = []
        for flight in flights:
            item = ListFlightDto()
            item.id = flight["id"]
            item.flight_number = flight["flight_number"]
            item.aircraft_number = flight["aircraft__aircraft_number"]
            item.take_off_point = flight["take_off_point"]
            item.destination = flight["destination"]
            item.price = flight["price"]
            item.flight_class = flight["flight_class"]
            result.append(item)
        return result

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        flights = Flight.objects.values("id", "flight_number")
        return [SelectOptionDto(f["id"], f["flight_number"]) for f in flights]

    def search_related_flight(self, take_off_point: str, take_off_time: date, destination: str) -> List[
        SearchFlightDetailsDto]:
        flights = Flight.objects
        if take_off_time is not None:
            flights = flights.filter(take_off_time__date=take_off_time)
        if take_off_point is not None:
            flights = flights.filter(take_off_point=take_off_point)
        if destination is not None:
            flights = flights.filter(destination=destination)

        flights = list(flights)
        results = []
        for flight in flights:
            result = SearchFlightDetailsDto()
            result.id = flight.id
            result.take_off_point = flight.take_off_point
            result.take_off_time = flight.take_off_time
            result.destination = flight.destination
            result.flight_number = flight.flight_number
            result.price = flight.price
            result.flight_class = flight.flight_class
            results.append(result)
        return results
