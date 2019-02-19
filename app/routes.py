#!/usr/bin/env python3
from app import app
from app import api_call
from app import parse_data


from flask import render_template
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    ## Creates a dictionary of dates to be used below
    timespans = api_call.define_request_timespan()

    ## remove the 'today' entry from dictionary and format it for the request
    temp1 = datetime.strptime(timespans['today'], '%Y-%m-%d')
    end_date = temp1.strftime('%b %d, %y')
    del timespans['today']

    ## empty dictionary for storing important data from the request
    data_dict = {}
    ## empty dict for formatted timespans (is this necessary?)
    formatted_timespans = {}

    ## for each timespan(day/week/month), make the request and extract data
    for key in timespans.keys():
        temp = datetime.strptime(timespans[key], '%Y-%m-%d')
        formatted_timespans[key] = temp.strftime('%b %d, %y')
        ## skip today because I don't want it
        if key != 'today':

            ## MAKE THE GET REQUEST
            
            ## the actual request and extracting data from files in data/
            file_name = key + '.json'
            raw = parse_data.load_data_file(file_name)
            data_dict[key] = parse_data.parse_response_data(raw)

            

    return render_template('index.html', 
                            data=data_dict, 
                            timespans=timespans, 
                            formatted_timespans=formatted_timespans, 
                            end_date=end_date
                            )
