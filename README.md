---

# Elvio Finder

Elvio Finder is a Python application designed to find locations based on latitude and longitude coordinates. It allows you to input coordinates (with directions for latitude and longitude) and outputs the corresponding location address. This project also includes a web interface that utilizes the Geopy library for geocoding and displays location details.

## Features:
- Accepts latitude and longitude coordinates, including directions (e.g., `6.7924S`, `39.2083E`).
- Returns location address for the given coordinates.
- Displays a Google Maps link for easy navigation.
- Provides location details in the terminal.
- Fetches location information from the browser using HTML and JavaScript.
- Supports both geolocation via IP and coordinates.

## Requirements:
- Python 3.x
- Geopy library
- Flask (for the web application)
- HTML, JavaScript (for the frontend)

## Installation:
1. Clone the repository or download the script.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Setup:
1. **Run the Flask application**:
   ```bash
   python app.py
   ```
2. Open the HTML page in a browser to request your location.

## Usage:
1. In the browser, click "Get My Location" to automatically get latitude and longitude from your browser's geolocation.
2. The server will fetch the location address and display the details in the terminal.
3. The location address and Google Maps link will be shown in the browser.

Example output:

- **Terminal**:
  ```
  Location details (from coordinates): Kigogo Road, Mabibo Relini, Mabibo, Ubungo Municipal, Dar es-Salaam, Coastal Zone, Tanzania
  Latitude: -6.8059136, Longitude: 39.2200192
  Google Maps Link: https://www.google.com/maps?q=-6.8059136,39.2200192
  ```
- **Browser**: Displays the location address and a link to Google Maps.

---

