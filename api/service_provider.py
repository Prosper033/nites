from dependency_injector import containers, providers

from api.repositories.AircraftRepository import AircraftRepository, DjangoORMAircraftRepository
from api.repositories.FlightRepository import DjangoORMFlightRepository, FlightRepository
from api.services.AircraftManagementService import AircraftManagementService, DefaultAircraftManagementService
from api.services.FlightManagementService import DefaultFlightManagementService, FlightManagementService
from api.services.PassengerManagementService import DefaultPassengerManagementService, PassengerManagementService
from api.repositories.PassenegrRepository import PassengerRepository, DjangoORMPassengerRepository
from api.repositories.BookingRepository import BookingRepository, DjangoORMBookingRepository
from api.services.BookingManagementService import BookingManagementService, DefaultBookingManagementService
from typing import Callable


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    flight_repository: Callable[[], FlightRepository] = providers.Factory(
        DjangoORMFlightRepository
    )

    aircraft_repository: Callable[[], AircraftRepository] = providers.Factory(
        DjangoORMAircraftRepository
    )

    flight_management_service: Callable[[], FlightManagementService] = providers.Factory(
        DefaultFlightManagementService,
        repository=flight_repository
    )

    aircraft_management_service: Callable[[], AircraftManagementService] = providers.Factory(
        DefaultAircraftManagementService,
        repository=aircraft_repository
    )

    passenger_repository: Callable[[], PassengerRepository] = providers.Factory(
        DjangoORMPassengerRepository
    )

    passenger_management_service: Callable[[], PassengerManagementService] = providers.Factory(
        DefaultPassengerManagementService,
        repository=passenger_repository
    )

    booking_repository: Callable[[], BookingRepository] = providers.Factory(
        DjangoORMBookingRepository
    )

    booking_management_service: Callable[[], BookingManagementService] = providers.Factory(
        DefaultBookingManagementService,
        repository=booking_repository
    )


api_service_container = Container()
