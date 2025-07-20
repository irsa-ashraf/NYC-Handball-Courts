'''
Helper functions
'''

import pandas as pd 
import numpy as np 
import folium 
import os 

current_directory = os.getcwd()
data_dir = os.path.join(os.path.dirname(current_directory), 'Data')

def create_map(data_df, center_lat, center_lon):
    '''
    '''

    nyc_map = folium.Map(location=[center_lat, center_lon], zoom_start=12.5)

    hb_data = pd.read_csv(os.path.join(data_dir, "handball_courts_clean.csv")) 

    for idx, row in data_df.iterrows():
        popup_text = f"""
        <strong>Court Name:</strong> {row['Name']}<br>
        <strong>Address:</strong> {row['Location']}<br>
        <strong>No. of Courts:</strong> {row['Num_of_Courts']}<br>
        """
        folium.Marker(location=[row['lat'], row['lon']], popup=folium.Popup(popup_text, max_width=300)).add_to(nyc_map)

    # Marking user location
    folium.Marker(
        location=[center_lat, center_lon],
        popup="You are here",
        icon=folium.Ison(color="red")  
    ).add_to(nyc_map)

    return nyc_map