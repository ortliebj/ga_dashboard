#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

from app import routes
from app import api_call
from app import parse_data