class CreateAircraftDto:
    aircraft_number: str
    name: str
    type: str
    capacity: int


class EditAircraftDto:
    id: int
    name: str
    type: str
    capacity: int
    aircraft_number: str


class AircraftDetailsDto:
    id: int
    aircraft_number: str
    name: str
    type: str
    capacity: int


class ListAircraftDto:
    id: int
    aircraft_number: str
    name: str
    type: str
    capacity: int
