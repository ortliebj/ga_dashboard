#!/usr/bin/env python3
import os
import sys
import json

def load_data_file(file_name):
    """
    parameter: the name of the file you want to read within the data/ folder
    return: the contents of the above file as a dictionary
    """

    ## get path of the data/ folder in main directory
    main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data/'
    ## the path of the file to be read
    response_file = os.path.join(main_dir, file_name)
    ## a dict to store the contents of the above file
    raw_data = {}

    ## create/open the above file
    with open(response_file, 'r') as f:
        raw_data = json.load(f)
    
    return raw_data


def parse_response_data(raw_data):
    """
    parameter: the raw data in dictionary form, most likely extracted with the above function
    returns: a dictionary of relevant metrics from GA
    """
    data = {}
    metric_headers = raw_data['reports'][0]['columnHeader']['metricHeader']['metricHeaderEntries']
    data_values = raw_data['reports'][0]['data']['rows'][0]['metrics'][0]['values']

    for i, item in enumerate(metric_headers):
        data[item['name'].strip('ga:')] = data_values[i]

    return data


def main():
    raw_data = load_data_file('day.json')
    data = parse_response_data(raw_data)
    print(data)


if __name__ == '__main__':
    main()