import requests

API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def main():
    city = input("Enter the city name: ")
    weather_data = get_weather(city)
    
    if weather_data.get("cod") != 200:
        print("City not found!")
    else:
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"Temperature: {temp}°C")
        print(f"Weather: {description.capitalize()}")

if __name__ == "__main__":
    main()