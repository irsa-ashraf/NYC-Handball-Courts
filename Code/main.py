'''
Application to start the server
'''

import pandas as pd
from flask import Flask, render_template
import os
import utils 

app = Flask(__name__)

# health check endpoint 
@app.route('/', methods = ["GET"])
def root():
    return "Hello World!"


# endpoint that reads handball court data and renders a map 
@app.route('/FindCourts', methods = ["GET"])
def find_courts():
    '''
    '''

    nyc_lat = 40.7128
    nyc_lon = -74.0060

    current_directory = os.getcwd()
    data_dir = os.path.join(os.path.dirname(current_directory), 'Data')
    
    hb_data = pd.read_csv(os.path.join(data_dir, "handball_courts_clean.csv"))

    nyc_map = utils.create_map(hb_data)

    # Save the map as an HTML file
    nyc_map.save('templates/map.html')

    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)