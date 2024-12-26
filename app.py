from flask import Flask, request
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.extra.rate_limiter import RateLimiter
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def find_location_by_coordinates(lat, lon):
    try:
        geolocator = Nominatim(user_agent="elvioLocationApp")
        reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1)
        location = reverse((lat, lon), language="en", zoom=18)
        return location.address if location else "No precise location found"
    except GeocoderTimedOut:
        return "Request timed out. Try again later."

@app.route('/get_location', methods=['GET'])
def get_location():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    if lat is not None and lon is not None:
        location = find_location_by_coordinates(lat, lon)
        if location and location != "No precise location found":
            print(f"Location details (from coordinates): {location}")
            print(f"Latitude: {lat}, Longitude: {lon}")
            print(f"Google Maps Link: https://www.google.com/maps?q={lat},{lon}")
            return "", 204
        else:
            print("Unable to retrieve precise location details.")
    else:
        print("Coordinates not provided or invalid.")
    return "", 204

if __name__ == '__main__':
    app.run(debug=True)
