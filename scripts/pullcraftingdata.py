from bs4 import BeautifulSoup
from flask import Flask
import json
import requests


with open('../json/TestItems.json') as jsonFile:
    items = json.load(jsonFile)

    for item in items['items']:
        url = 'https://www.albion-online-data.com/api/v1/stats/Prices/' + item['name'] + '?'
        response = requests.get(url, timeout=10)
        objects = response.json()

        output = item['name'] + ": " + item['description'] + ": "
        for obj in objects:
            # if obj['city'] == "Black Market" or obj['city'] == "Caerleon":
            if obj['city'] != "Mountain Cross" and obj['city'] != "Steppe Cross" and obj['city'] != "Forest Cross" and obj['city'] != "Highland Cross" and obj['city'] != "Swamp Cross":
                output2 = str(obj['sell_price_min']) + " " + obj['city'] + ": "
                output = output + output2
        print(output)
