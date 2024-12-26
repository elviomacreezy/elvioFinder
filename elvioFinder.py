import geopy
from geopy.geocoders import Nominatim
import requests

def find_location_by_coordinates(lat, lon):
    geolocator = Nominatim(user_agent="elvioLocationApp")
    location = geolocator.reverse((lat, lon), language='en')
    return location.address

def find_location_by_ip(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    if response.status_code == 200:
        data = response.json()
        if "loc" in data:
            lat, lon = map(float, data["loc"].split(","))
            return lat, lon, data
    return None, None, None

def get_ip_address():
    ip = requests.get('https://api.ipify.org').text
    return ip

print("""
----------------------------------------
           Elvio Finder
----------------------------------------
""")

choice = input("Select 'i' for IP address or 'c' for coordinates: ").strip().lower()

if choice == "i":
    ip_address = input("Enter the IP address or press Enter to use your own IP: ").strip()
    if not ip_address:
        ip_address = get_ip_address()
    lat, lon, data = find_location_by_ip(ip_address)
    if lat is not None and lon is not None:
        location = find_location_by_coordinates(lat, lon)
        google_maps_link = f"https://www.google.com/maps?q={lat},{lon}"
        print("\nLocation Information:")
        print(f"Address: {location}")
        print(f"Google Maps Link: {google_maps_link}")
        print("\nIP Information:")
        print(f"IP Address: {data.get('ip', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location: {data.get('loc', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
        print(f"Timezone: {data.get('timezone', 'N/A')}")
    else:
        print("Could not find location for the given IP address.")
elif choice == "c":
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
    location = find_location_by_coordinates(lat, lon)
    google_maps_link = f"https://www.google.com/maps?q={lat},{lon}"
    print("\nLocation Information:")
    print(f"Address: {location}")
    print(f"Google Maps Link: {google_maps_link}")
else:
    print("Invalid choice. Please enter 'i' for IP or 'c' for coordinates.")
