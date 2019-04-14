## Google Analytics Dashboard

This is a simple dashboard to display Google Analytics pageviews for the past 
day, week, and month on a local webpage.

### Prerequites
Python 3.6 or later, pip, and venv (or another virtual environment).

### Installation

Download the files and unzip them, or clone this repo to a folder on your
computer. cd to that directory, then create a virtual environmnet with:
```
python3 -m venv env
```
Activate the environment:
```
source bin/env/activate
```
Install the required packages:
```
pip3 install -r requirements.txt
```
### Setup
Create an application on [Google's Developer Site](https://developers.google.com/)
and download the client_secrets.json file. Copy that into secrets/. Find your
Google Analytics view ID to copy into app/api_call.py as the VIEW_ID variable.

### Deployment
At the moment, you need to run api_call and parse_data manually whenever 
you want the data to update. You could of course schedule this in the terminal,
I just haven't done that yet. Anyways, `python3 api_call.py` followed by
`parse_data.py` will create a data/ folder in the main directory if run for 
the first time or replace what's there any time after that. Run the 
flask app with `python3 run.py` and open a browser to http://0.0.0.0/8080 to
see the data.
