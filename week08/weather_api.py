"""Client and formatters for the WeatherAPI.com service."""

import requests


class WeatherAPI:
    """Small wrapper around the WeatherAPI.com REST endpoints."""

    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def _get(self, endpoint, params):
        """Send a GET request and return parsed JSON, or None on failure."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

    def get_current_weather(self, location):
        """Return current weather data for a location."""
        return self._get("current.json", {"key": self.api_key, "q": location})

    def get_forecast(self, location, days=3):
        """Return forecast data for a location (1-3 days)."""
        if not 1 <= days <= 3:
            raise ValueError("days must be between 1 and 3")
        return self._get(
            "forecast.json", {"key": self.api_key, "q": location, "days": days}
        )


def format_current_weather(data):
    """Format current weather as 'CITY, COUNTRY: TEMP°F, CONDITION'."""
    location = data["location"]
    current = data["current"]
    return (
        f"{location['name']}, {location['country']}: "
        f"{current['temp_f']}°F, {current['condition']['text']}"
    )


def format_forecast(data):
    """Format each forecast day as 'DATE: high TEMP°F, low TEMP°F, CONDITION'."""
    lines = []
    for day in data["forecast"]["forecastday"]:
        info = day["day"]
        lines.append(
            f"{day['date']}: high {info['maxtemp_f']}°F, "
            f"low {info['mintemp_f']}°F, {info['condition']['text']}"
        )
    return "\n".join(lines)
