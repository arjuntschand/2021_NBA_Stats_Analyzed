import math
import pandas as pd
import numpy as np # linear algebra
import requests
import json
import mysql.connector

playerid = 1

response = requests.get('https://www.balldontlie.io/api/v1/season_averages?player_ids[]=237')

playerid += 1
