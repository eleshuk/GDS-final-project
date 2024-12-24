# Author: Elizabeth Leshuk/Open-Meteo
# Code to access data from Open-Meteo

import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

def get_historical_weather_data(lat, long, date_start, date_end):
    # Latitude and longitude
# lat = 39.3999
# long = -8.2245

	# Setup the Open-Meteo API client with cache and retry on error
	cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
	retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
	openmeteo = openmeteo_requests.Client(session = retry_session)

	# Make sure all required weather variables are listed here
	# The order of variables in hourly or daily is important to assign them correctly below
	url = "https://archive-api.open-meteo.com/v1/archive"
	params = {
	"latitude": lat,
	"longitude": long,
	"start_date": date_start,
	"end_date": date_end,
	"hourly": ["temperature_2m", "relative_humidity_2m"]
	}
	responses = openmeteo.weather_api(url, params=params)

	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]
	print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
	print(f"Elevation {response.Elevation()} m asl")
	print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
	print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

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

	# Access data
	data_path = config['raw_data']

	hourly_dataframe.to_csv(data_path+'raw_weather_data.csv', index=False) 


	# Access data
	data_path = config['raw_data']
	hourly_dataframe.to_csv(data_path+'raw_historical_weather_data.csv', index=False) 


