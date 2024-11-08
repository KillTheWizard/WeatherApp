
# Weather App

This Python Weather App fetches and displays real-time weather data for a specified city using the OpenWeatherMap API.

## Features

- Retrieves live weather data for a given city
- Displays temperature in Celsius and a description of the weather conditions
- Error handling for invalid city names

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using:
```
pip install requests
```

## Setup

1. Clone this repository or download the `weather_app.py` file.
2. Obtain an API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
3. Insert your API key into the `API_KEY` variable in `weather_app.py`.

## Usage

1. Run the application with:
    ```
    python weather_app.py
    ```
2. Enter the name of the city when prompted, and the app will display the current temperature and weather conditions.

## Example Output

```plaintext
Enter the city name: Houston
Temperature: 25°C
Weather: Clear sky
```

## Note

Make sure your API key is kept secure. Avoid hardcoding it in the file for public repositories.
