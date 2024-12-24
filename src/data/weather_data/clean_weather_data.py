import pandas as pd
from datetime import datetime
import yaml
import os

def classify_day_night(row):
    # Ensure sunrise, sunset, and timestamp are tz-aware (they should already be if you followed the above steps)
    sunrise = row['sunrise']
    sunset = row['sunset']
    timestamp = row['timestamp']
    
    # Classify as 'day' or 'night'
    if sunrise <= timestamp < sunset:
        return 'day'
    else:
        return 'night'

def clean_and_merge():
    # Relative path to the root-level file
    config_path = os.path.join("..", "..", "..", "config.yml")
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    # Get data paths
    raw_data_filepath = config['raw_data']
    sunset_sunrise_filepath = raw_data_filepath+"sunset_sunrise.csv"
    weather_filepath = raw_data_filepath+"raw_historical_weather_data.csv"

    # Combine day/night data with temperature data
    # Read in both dfs
    sunset_sunrise = pd.read_csv(sunset_sunrise_filepath, index_col=None)
    weather_data = pd.read_csv(weather_filepath)

    # Drop column unnamed
    sunset_sunrise = sunset_sunrise.drop(columns=["Unnamed: 0"])
    # Drop na
    clean_weather = weather_data.dropna()

    # Convert 'sunrise' and 'sunset' to datetime with timezone-awareness (e.g., UTC)
    sunset_sunrise['sunrise'] = pd.to_datetime(sunset_sunrise['sunrise'], utc=True)
    sunset_sunrise['sunset'] = pd.to_datetime(sunset_sunrise['sunset'], utc=True)
    sunset_sunrise['date'] = pd.to_datetime(sunset_sunrise['date']).dt.date

    # Create column "timestamp"
    clean_weather = clean_weather.copy()
    clean_weather.loc[:, 'timestamp'] = pd.to_datetime(clean_weather['date'])

    # Convert date column to match sunrise data
    clean_weather.loc[:, 'date'] = pd.to_datetime(clean_weather['date']).dt.strftime('%Y-%m-%d')

    # Update date format
    clean_weather['date'] = pd.to_datetime(clean_weather['date'])
    sunset_sunrise['date'] = pd.to_datetime(sunset_sunrise['date'])

    # Merge data
    merged_data = pd.merge(clean_weather, sunset_sunrise, on='date', how='inner')

    # Add column that sets day or night value based on sunset on that day
    merged_data['day_night'] = merged_data.apply(classify_day_night, axis=1)

    # Get average day and night time temperatures
    average_temps_by_date = merged_data.groupby(['date', 'day_night'])['temperature_2m'].mean().unstack()

    # Reset index
    average_temps_by_date = average_temps_by_date.reset_index()

    # Write output to data folder
    processed_data = config['top_level']+"data/processed/average_temps_by_date.csv"
    average_temps_by_date.to_csv(processed_data, index=True)

    