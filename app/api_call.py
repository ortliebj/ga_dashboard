#!/usr/bin/env python3
import sys
import json

from datetime import date, timedelta

import google.auth
from googleapiclient.discovery import build
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials

VIEW_ID = 'YOUR VIEW ID'

def define_request_timespan():
    '''
    returns: a dictionary of strings of timespans formatted like so:
        {'today': '2019-01-11', 'day': '2019-01-10', 'month': '2018-12-11'}
    '''
    today = date.today()
    timespans = {'today' : today.strftime('%Y-%m-%d'),
                 'Day'   : (today - timedelta(days=1 )).strftime('%Y-%m-%d'),
                 'Week'  : (today - timedelta(days=7 )).strftime('%Y-%m-%d'),
                 'Month' : (today - timedelta(days=30)).strftime('%Y-%m-%d')    
                }

    return timespans


def get_credentials():
    '''
    This function's only purpose is to get credentials from Google
    as a service account.
    Returns a scoped instance of Credentials.
    '''
    scopes = ['https://www.googleapis.com/auth/analytics.readonly']

    ## attempt to get credentials
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'secrets/client_secrets.json', scopes)
    ## TODO: catch specific errors
    except: 
        print('something went wrong creating the credentials')
        sys.exit(0)
    
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics


def get_request(analytics, start_date, end_date):
    """
    parameters: analytics returned from get_credentials(),
                start date for the range for data,
                end date for the range for data
    returns:    json response
    todo: add specific exceptions
    """
    request_body = {
        "reportRequests": 
        [
            {
                "viewId": VIEW_ID,
                "includeEmptyRows": True,
                "dateRanges": 
                [   
                    {
                        "startDate": start_date, 
                        "endDate": end_date
                    }
                ],
                "metrics": 
                [
                    {
                        "expression": "ga:users"
                    },
                    {
                        "expression": "ga:pageViews",
                    }
                ]
            }
        ]
    }

    try:
        responses = analytics.reports().batchGet(body=request_body).execute()
    except:
        print('failed to GET')
        sys.exit(0)

    return responses
    

def save_response_to_file(response, file_name):
    """
    save the raw response to a file in data/ folder
    """
    formatted_file = 'data/{}.json'.format(file_name)
    with open(formatted_file, 'w') as f:
        json.dump(response, f)


def main():
    analytics = get_credentials()
    timespans = define_request_timespan()

    today = timespans['today']
    
    for key, val in timespans.items():
        if key != 'today':
            response = get_request(analytics, val, today)
            save_response_to_file(response, key)
    
    
if __name__ == '__main__':
    main()
