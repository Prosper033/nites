from datetime import date


class CreateFlightDto:
    aircraft_id: int
    flight_number: str
    take_off_point: str
    take_off_time: date
    destination: str
    price: float
    flight_class: str


class EditFlightDto:
    id: int
    aircraft_id: int
    take_off_point: str
    take_off_time: date
    destination: str
    price: float
    flight_class: str


class ListFlightDto:
    id: int
    flight_number: str
    aircraft_number: int
    take_off_point: str
    destination: str
    price: float
    flight_class: str


class FlightDetailsDto:
    id: int
    aircraft_id: int
    flight_number: str
    take_off_point: str
    take_off_time: date
    destination: str
    price: float
    flight_class: str


class SearchFlightDetailsDto:
    id: int
    aircraft_id: int
    flight_number: str
    take_off_point: str
    take_off_time: date
    destination: str
    price: float
    flight_class: str
