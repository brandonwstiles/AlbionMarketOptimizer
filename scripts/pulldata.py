import requests as requests
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

        try:
            profits = objects[0]['sell_price_min'] - objects[2]['sell_price_min']
        except IndexError:
            profits = 0

        profits = profits - (objects[0]['sell_price_min'] * .06)
        output = item['name'] + ": " + item['description'] + ": "

        if profits > 0 and ((0 < objects[0]['sell_price_min'] < 50000) and (0 < objects[1]['sell_price_min'] < 50000)):
            # print(item['name'] + ": " + item['description'])
            for obj in objects:
                if obj['city'] == "Black Market" or obj['city'] == "Caerleon":
                    # bj['city'] == "Mountain Cross" and obj['city'] != "Steppe Cross" and obj['city'] != "Forest Cross" and obj['city'] != "Highland Cross":
                    output2 =  str(obj['sell_price_min']) +  " " + obj['city'] + ": "
                    output = output + output2
            output3 = ("Profit: " + str(profits))
            output = output + output3
            print(output)
