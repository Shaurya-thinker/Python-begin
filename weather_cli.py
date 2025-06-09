import requests
import sys

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)

        data = response.json()

        # Extract and display weather info
        print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
        print(f"🌡 Temperature: {data['main']['temp']} °C")
        print(f"🌥 Description: {data['weather'][0]['description'].title()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🌬 Wind Speed: {data['wind']['speed']} m/s\n")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Network error: {err}")
    except KeyError:
        print("Unexpected data format. Are you sure the city name is valid?")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python weather_cli.py <CITY_NAME> <API_KEY>")
        sys.exit(1)

    city = sys.argv[1]
    api_key = sys.argv[2]

    get_weather(city, api_key)

if __name__ == "__main__":
    main()