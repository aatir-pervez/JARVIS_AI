import requests
from core.speak import speak

def get_coordinates(city):
    try:
        # 🌍 Geocoding API (no key needed)
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        
        response = requests.get(url)
        data = response.json()

        if "results" not in data:
            return None, None

        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]

        return lat, lon

    except Exception as e:
        print("Geocoding error:", e)
        return None, None


def get_weather(city="kolkata"):
    try:
        lat, lon = get_coordinates(city)

        if lat is None or lon is None:
            speak("Sorry, I couldn't find that location")
            return

        # 🌦️ Weather API
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

        response = requests.get(url)
        data = response.json()

        temp = round(data["current_weather"]["temperature"])  #  rounded
        wind = data["current_weather"]["windspeed"]
        

        speak(f"The current temperature in {city} is around {temp} degrees Celsius")
        speak(f"Wind speed is {wind} kilometers per hour")

    except Exception as e:
        print("Weather error:", e)
        speak("Sorry, I couldn't fetch the weather")