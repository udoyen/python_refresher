# Python standard libraries
import json
import os
import sqlite3

# Third-party libraries
from flask import Flask, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

# Internal imports
from db import init_db_command
from user import User
from google-info import myinfo

# Configuration
GOOGLE_CLIENT_ID = os.environ.get(myinfo['GOOGLE_CLIENT_ID'], None)
GOOGLE_CLIENT_SECRET = os.environ.get(myinfo["GOOGLE_CLIENT_SECRET"], None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)