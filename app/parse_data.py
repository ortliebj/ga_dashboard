#!/usr/bin/env python3
import os
import sys
import json

def load_data_file(file_name):
    main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data/'
    response_file = os.path.join(main_dir, file_name)
    raw_data = {}

    with open(response_file, 'r') as f:
        raw_data = json.load(f)
    
    return raw_data


def parse_response_data(raw_data):
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