from typing import NamedTuple
from bs4 import BeautifulSoup
import requests
import country_converter as coco
from geopy.geocoders import Nominatim
from exceptions import CantGetCoordinates, CantGetLocation
import platform
from subprocess import Popen, PIPE


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_location():
    url = 'https://www.iplocation.net/find-ip-address'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    ip_span = soup.find('table', class_='iptable')
    # ip_ = ip_span.find('td').text.split()[0]
    loc = ip_span.find_all('td')[2].text.split()[:-1]
    city = loc[0][:-1]
    country = coco.convert(names=loc[-1][1:-1], to='name_short')
    if not city or not country:
        raise CantGetLocation
    return city, country




def get_coordinates() -> Coordinates:
    global latitude, longitude
    os_ = platform.system()
    if os_ == 'Windows':
        """Returns current coordinates using Windows PC"""
        location: tuple[str, str | list[str]] = get_location()
        geolocator = Nominatim(user_agent='myapplication')
        location = geolocator.geocode(location)
        latitude = location.raw['lat']
        longitude = location.raw['lon']
        if location.raw['lon'] == 0 or location.raw['lat'] == 0:
            raise CantGetCoordinates
    # elif os_ == 'Darwin':
    #     """Returns current coordinates using MacBook"""
    #     process = Popen(['whereami'], stdout=PIPE)
    #     (output, err) = process.communicate()
    #     exit_code = process.wait()
    #     if err is not None or exit_code != 0 :
    #         raise CantGetCoordinates
    #     output_lines = output.decode().strip().lower().split('\n')
    #     latitude = longitude = None
    #     for line in output_lines:
    #         if line.startswith('latitude:'):
    #             latitude = float(line.split()[1])
    #         if line.startswith('longitude:'):
    #             longitude = float(line.split()[1])

    return Coordinates(latitude=latitude, longitude=longitude)



