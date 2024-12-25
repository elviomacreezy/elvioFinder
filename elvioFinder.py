import geopy
from geopy.geocoders import Nominatim

def find_location(lat, lon):
    geolocator = Nominatim(user_agent="elvioLocationApp")
    location = geolocator.reverse((lat, lon), language='en')
    return location.address

print("""
----------------------------------------
           Elvio Finder
----------------------------------------
""")
lat_input = input("Enter latitude: ")
lon_input = input("Enter longitude: ")

lat = float(lat_input[:-1])
lon = float(lon_input[:-1])

if 'S' in lat_input:
    lat = -abs(lat)
if 'N' in lat_input:
    lat = abs(lat)
if 'W' in lon_input:
    lon = -abs(lon)
if 'E' in lon_input:
    lon = abs(lon)

location = find_location(lat, lon)
print(location)
