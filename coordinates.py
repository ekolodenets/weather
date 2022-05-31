from typing import NamedTuple

class Coordinates(NamedTuple):
    latitude: float
    longitude: float

def get_coordinates() -> Coordinates:
    return Coordinates(latitude=10, longitude=20)