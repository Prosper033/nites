from abc import ABCMeta, abstractmethod
from typing import List

from api.repositories.PassenegrRepository import PassengerRepository
from api.dto.PassengerDto import ListPassengerDto, PassengerDetailsDto, EditPassengerDto, CreatePassengerDto
from api.dto.CommonDto import SelectOptionDto


class PassengerManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_passenger(self, model: CreatePassengerDto):
        """Create Passenger Object"""
        raise NotImplementedError

    def list_passenger(self) -> List[ListPassengerDto]:
        """List Passenger Object"""
        raise NotImplementedError

    def edit_passenger(self, name: str, model: EditPassengerDto):
        """Edit Passenger object"""
        raise NotImplementedError

    def passenger_details(self, name: str) -> PassengerDetailsDto:
        """Get Passenger Object"""
        raise NotImplementedError

    def delete_passenger(self, name: str):
        """Delete Passenger object"""
        raise NotImplementedError

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        """Creates a passsenger object"""
        raise NotImplementedError


class DefaultPassengerManagementService(PassengerManagementService):
    repository: PassengerRepository

    def __init__(self, repository: PassengerRepository):
        self.repository = repository

    def create_passenger(self, model: CreatePassengerDto):
        return self.repository.create_passenger(model)

    def list_passenger(self) -> List[ListPassengerDto]:
        return self.repository.list_passenger()

    def passenger_details(self, name: str) -> PassengerDetailsDto:
        return self.repository.passenger_details(name)

    def delete_passenger(self, name: str):
        return self.repository.delete_passenger(name)

    def edit_passenger(self, name: str, model: EditPassengerDto):
        return self.repository.edit_passenger(name, model)

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        return self.repository.get_all_for_select_list()
