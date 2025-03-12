

from langchain.tools import Tool
from langchain.tools import WikipediaQueryRun
from langchain.utilities import OpenWeatherMapAPIWrapper
import requests

# API Tool definition
import os
from dotenv import load_dotenv
from langchain.tools import Tool

# Load environment variables from .env file
load_dotenv()


class WeatherTool:
    def __init__(self):
        weather_api_key = os.getenv('OPENWEATHERMAP_API_KEY')
        if not weather_api_key:
            raise ValueError("OPENWEATHERMAP_API_KEY environment variable is not set.")
        

        weather = OpenWeatherMapAPIWrapper()

        self.weather_tool = Tool(
            name="Weather Lookup",
            func= weather.run,
            description="Provides real-time weather updates for a given city."
        )

    def get_tool(self):
        return self.weather_tool



