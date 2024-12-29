# Create list of municipalities
import pandas as pd

def get_municipalities_list():
    municipalities_file = "/Users/eleshuk/Library/CloudStorage/GoogleDrive-eleshuk@gmail.com/.shortcut-targets-by-id/1XNkQR60z1T7WELqvqkvZchRrVWQpCzvs/data_science_project/Project Template/data/raw/Weather/Municipal Boundaries of Portugal.csv"

    # Load municipalities data
    municipalities_data = pd.read_csv(municipalities_file)

    # Filter the DataFrame to find the corresponding row
    # matching_row = municipalities_data[municipalities_data['Name'].str.lower() == user_input.lower()]

    # # Check if a match was found
    # if not matching_row.empty:
    #     latitude = matching_row.iloc[0]['Latitude'].round(2)
    #     longitude = matching_row.iloc[0]['Longitude'].round(2)
    #     # print(f"The latitude and longitude of {user_input} are: ({latitude}, {longitude})")
    
    # return [latitude, longitude]

    municipalities_list = municipalities_data['Name'].tolist()

    return municipalities_list
