from abc import ABCMeta, abstractmethod
from typing import List

from api.dto.AircraftDto import AircraftDetailsDto, CreateAircraftDto, EditAircraftDto, ListAircraftDto
from api.models import Aircraft
from api.dto.CommonDto import SelectOptionDto


class AircraftRepository(metaclass=ABCMeta):
    @abstractmethod
    def create(self, model: CreateAircraftDto):
        """Create a Aircraft Object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditAircraftDto):
        """Edit a Aircraft object"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, aircraft_id: int):
        """Delete a Aircraft object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListAircraftDto]:
        """Get List of Aircraft"""
        raise NotImplementedError

    @abstractmethod
    def get(self, aircraft_id: int) -> AircraftDetailsDto:
        """An Aircraft detail"""
        raise NotImplementedError

    @abstractmethod
    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Creates a aircraft object"""
        raise NotImplementedError


class DjangoORMAircraftRepository(AircraftRepository):
    def create(self, model: CreateAircraftDto):
        aircraft = Aircraft()
        aircraft.name = model.name
        aircraft.aircraft_number = model.aircraft_number
        aircraft.type = model.type
        aircraft.capacity = model.capacity
        aircraft.save()

    def edit(self, id: int, model: EditAircraftDto):
        try:
            aircraft = Aircraft.objects.get(id=id)
            aircraft.name = model.name
            aircraft.type = model.type
            aircraft.capacity = model.capacity
            aircraft.save()
        except Aircraft.DoesNotExist as e:
            message = "Tried to update a aircraft that dose not exit"
            print(message)
            raise e

    def delete(self, aircraft_id: int):
        try:
            aircraft = Aircraft.objects.filter(id=aircraft_id).delete()
        except Aircraft.DoesNotExist as e:
            message = "Tried to delete a aircraft that dose not exit"
            print(message)
            raise e

    def get(self, aircraft_id: int) -> AircraftDetailsDto:
        try:
            aircraft = Aircraft.objects.get(id=aircraft_id)
            result = AircraftDetailsDto()
            result.id = aircraft.id
            result.aircraft_number = aircraft.aircraft_number
            result.name = aircraft.name
            result.type = aircraft.type
            result.capacity = aircraft.capacity
            return result
        except Aircraft.DoesNotExist as e:
            message = "Tried aircraft dose not exit"
            print(message)
            raise e

    def list(self) -> List[ListAircraftDto]:
        aircrafts = list(Aircraft.objects.values("id",
                                                 "aircraft_number",
                                                 "type",
                                                 "capacity",
                                                 "name"))

        result: List[ListAircraftDto] = []
        for aircraft in aircrafts:
            item = ListAircraftDto()
            item.id = aircraft["id"]
            item.aircraft_number = aircraft["aircraft_number"]
            item.type = aircraft["type"]
            item.name = aircraft["name"]
            item.capacity = aircraft["capacity"]
            result.append(item)
        return result

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        aircraft = Aircraft.objects.values("id", "aircraft_number")
        return [SelectOptionDto(a["id"], a["aircraft_number"]) for a in aircraft]

