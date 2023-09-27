import json
import requests
from bs4 import BeautifulSoup
import pandas as pd


keys = pd.read_csv('api.csv').to_dict(orient="records")
api_key = [item['key'] for item in keys if item['Service'] == 'OpenWeather'][0]

lat = '47.675510'
lon = '-122.203360'
units = 'metric'

url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units={units}"

response = requests.get(url=url)
response.raise_for_status()
data = response.json()
print(json.dumps(data['list']))
