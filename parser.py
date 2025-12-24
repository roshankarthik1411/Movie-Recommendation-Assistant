"""
Weather data parser module.
Handles parsing and validation of weather API responses.
"""

from typing import Dict, Any


class WeatherParser:
    """Parser for weather API responses."""
    
    def parse_weather_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse raw weather API response into structured format."""
        # TODO: Extract city name from raw_data.get('name')
        # TODO: Extract country from raw_data.get('sys', {}).get('country')
        # TODO: Extract temperature from raw_data.get('main', {}).get('temp')
        # TODO: Extract feels_like from raw_data.get('main', {}).get('feels_like')
        # TODO: Extract humidity from raw_data.get('main', {}).get('humidity')
        # TODO: Extract description from raw_data.get('weather', [])[0].get('description')
        # TODO: Extract wind_speed from raw_data.get('wind', {}).get('speed')
        # TODO: Return dictionary with all extracted data
        pass
    
    def validate_weather_data(self, weather_data: Dict[str, Any]) -> bool:
        """Validate that weather data has required fields."""
        # TODO: Check if required fields exist and are not None
        # TODO: Required fields: 'city', 'temperature', 'description', 'humidity', 'wind_speed'
        # TODO: Return True if all fields are present, False otherwise
        pass
    
    def format_weather_for_llm(self, weather_data: Dict[str, Any]) -> str:
        """Format weather data for LLM prompt."""
        # TODO: Create formatted string with weather information
        # TODO: Include city, country, temperature, feels_like, description, humidity, wind_speed
        # TODO: Add appropriate units (°C, %, m/s)
        # TODO: Return formatted string
        pass
