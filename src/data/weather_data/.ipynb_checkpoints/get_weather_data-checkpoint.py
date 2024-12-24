# Author: Elizabeth Leshuk/Open-Meteo
# Code to access data from Open-Meteo

# Input will later be user input, but for now use default coordinated - middle of PT

import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from datetime import datetime, timedelta, date

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# # Allowed range from 2016-01-01 to 2024-12-29"
# # This will be user input?
end_date = date.today()
start_date = end_date - timedelta(days=5)

# Latitude and longitude
lat = 39.3999
long = -8.2245

# Do we need historical data for modeling?

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 39.3999,
	"longitude": -8.2245,
    "start_date": start_date,
    "end_date": end_date,
	"hourly": ["temperature_2m", "relative_humidity_2m"]
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
# print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
# print(f"Elevation {response.Elevation()} m asl")
# print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
# print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)

import yaml
# Load the YAML file
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

# Access config data
data_path = config['raw_data']

hourly_dataframe.to_csv(data_path+'raw_weather_data.csv', index=False) 

