class CantGetCoordinates(Exception):
    """Program can't get current GPS coordinates"""


class CantGetLocation(Exception):
    """Program can't get current location"""


class ApiServiceError(Exception):
    """Programm can't get current weather"""