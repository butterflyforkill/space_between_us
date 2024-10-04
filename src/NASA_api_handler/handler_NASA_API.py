import requests
import json
from config.config_files import Settings


APOD_URL = 'https://api.nasa.gov/planetary/apod?api_key=' + Settings.APIkey


def get_nasa_data(date=None):
    url = APOD_URL
    if date:
        url += f"&date={date}"
    
    response = requests.get(url)
    response.raise_for_status()
    data_json = response.json()
    
    return {
        'title': data_json['title'],
        'description': data_json['explanation'],
        'image': data_json['url']
    }
