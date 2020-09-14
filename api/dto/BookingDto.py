from datetime import date


class CreateBookingDto:
    flight_id: int
    passenger_id: int
    booking_reference: str
    take_off_point: str
    take_off_time: date
    destination: str
    flight_class: str
    price: float
    name: str
    phone: str
    email: str
    address: str


class EditBookingDto:
    id: int
    flight_id: int
    passenger_id: int
    take_off_point: str
    take_off_time: date
    destination: str
    flight_class: str
    price: float
    booking_reference: str
    name: str
    phone: str
    email: str
    address: str


class ListBookingDto:
    id: int
    flight_number: str
    passenger_name: str
    booking_reference: str
    take_off_point: str
    take_off_time: date
    destination: str
    flight_class: str
    price: float
    name: str
    phone: str
    email: str
    address: str


class GetBookingDto:
    id: int
    flight_id: int
    passenger_id: int
    booking_reference: str
    take_off_point: str
    take_off_time: date
    destination: str
    flight_class: str
    price: float
    name:str
    phone: str
    email: str
    address: str











