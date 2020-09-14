from abc import ABCMeta, abstractmethod
from typing import List

from api.dto.PassengerDto import CreatePassengerDto, EditPassengerDto, ListPassengerDto, PassengerDetailsDto
from api.dto.CommonDto import SelectOptionDto
from api.models import Passenger


class PassengerRepository(metaclass=ABCMeta):
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
        """Creates a passenger object"""
        raise NotImplementedError


class DjangoORMPassengerRepository(PassengerRepository):

    def create_passenger(self, model: CreatePassengerDto):
        passenger = Passenger()
        passenger.name = model.name
        passenger.phone = model.phone
        passenger.address = model.address
        passenger.email = model.email
        passenger.save()

    def list_passenger(self) -> List[ListPassengerDto]:
        passengers = list(Passenger.objects.values('name',
                                                   'phone',
                                                   'address',
                                                   'email'))

        result: List[ListPassengerDto] = []
        for passenger in passengers:
            item = ListPassengerDto()
            item.name = passenger["name"]
            item.phone = passenger["phone"]
            item.address = passenger["address"]
            item.email = passenger["email"]
            result.append(item)
        return result

    def edit_passenger(self, name: str, model: EditPassengerDto):
        try:
            passenger = Passenger.objects.get(name=name)
            passenger.name = model.name
            passenger.phone = model.phone
            passenger.address = model.address
            passenger.email = model.email
            passenger.save()
        except Passenger.DoesNotExist as e:
            message = "Tried Passenger dose not exist"
            print(message)
            raise e

    def passenger_details(self, name: str) -> PassengerDetailsDto:
        try:
            passenger = Passenger.objects.get(name=name)
            result = PassengerDetailsDto()
            result.name = passenger.name
            result.phone = passenger.phone
            result.address = passenger.address
            result.email = passenger.email
            return result
        except Passenger.DoesNotExist as e:
            message = "Tried Passenger dose not exit"
            print(message)
            return e

    def delete_passenger(self, name: str):
        try:
            passenger = Passenger.objects.get(name)
            passenger.delete()
        except Passenger.DoesNotExist as e:
            message = "Tried Passenger dose not exit"
            print(message)
            return e

    def get_all_for_select_list(self) -> List[SelectOptionDto]:
        passengers = Passenger.objects.values("id", "name")
        return [SelectOptionDto(p["id"], p["name"]) for p in passengers]
