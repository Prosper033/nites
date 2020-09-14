from abc import ABCMeta, abstractmethod
from typing import List, Callable

from api.dto.AircraftDto import EditAircraftDto, AircraftDetailsDto, ListAircraftDto, CreateAircraftDto
from api.repositories.AircraftRepository import AircraftRepository
from api.dto.CommonDto import SelectOptionDto


class AircraftManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create(self, model: CreateAircraftDto):
        """Create a Aircraft Object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: int, model: EditAircraftDto):
        """Edit a Aircraft object"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, flight_id: int):
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


class DefaultAircraftManagementService(AircraftManagementService):
    repository: AircraftRepository = None

    def __init__(self, repository: AircraftRepository):
        self.repository = repository

    def create(self, model: CreateAircraftDto):
        return self.repository.create(model)

    def edit(self, id: int, model: EditAircraftDto):
        return self.repository.edit(id, model)

    def delete(self, aircraft_id: int):
        return self.repository.delete(aircraft_id)

    def get(self, aircraft_id: int) -> AircraftDetailsDto:
        return self.repository.get(aircraft_id)

    def list(self) -> List[ListAircraftDto]:
        return self.repository.list()

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()
