import requests
import pandas as pd  # Currently unused, but OK to keep if you’ll use it later

# API Key (only one used here)
API_KEY = '11f6aea29ef3ef399dc4fec98992fba7'

# --- Method 1: By City Name ---
city = 'Lira,UG'  # No space before "UG"
url_city = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

response_city = requests.get(url_city)

if response_city.status_code == 200:
    data = response_city.json()
    print(f"[City Lookup] Weather in {city}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C\n")
else:
    print("City-based request failed:", response_city.status_code)


# --- Method 2: By Coordinates ---
lat = 0.3476
lon = 32.5825
url_coords = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'

response_coords = requests.get(url_coords)

if response_coords.status_code == 200:
    data = response_coords.json()
    print(f"[Coordinates Lookup] Weather in {data['name']}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
else:
    print("Coordinates-based request failed:", response_coords.status_code)
    print("Response:", response_coords.text)
