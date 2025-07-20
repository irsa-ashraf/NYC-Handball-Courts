'''
Application to start the server
'''

import pandas as pd
from flask import Flask, render_template, request
import json
import os
import utils 

app = Flask(__name__)

# health check endpoint 
@app.route('/', methods = ["GET"])
def root():
    return "Hello World!"


# endpoint that reads handball court data and renders a map 
@app.route('/FindCourts', methods = ["GET", "POST"])
def find_courts():
    '''
    '''

    default_lat = 40.7128
    default_lon = -74.0060

    if request.method == "POST":
        try:
            user_location = request.get_json()
            user_lat = float(user_location.get('lat', default_lat))
            user_lon = float(user_location.get('lon', default_lon))
        except Exception as e:
            user_lat, user_lon = default_lat, default_lon
    else:
        user_lat, user_lon = default_lat, default_lon

    current_directory = os.getcwd()
    data_dir = os.path.join(os.path.dirname(current_directory), 'Data')
    
    hb_data = pd.read_csv(os.path.join(data_dir, "handball_courts_clean.csv"))

    nyc_map = utils.create_map(hb_data, user_lat, user_lon)

    # Save the map as an HTML file
    nyc_map.save('templates/map.html')

    return render_template('map.html')





if __name__ == '__main__':
    app.run(debug=True)