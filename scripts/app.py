import json

import requests
from flask_table import Table, Col, LinkCol
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

"""A example for creating a simple table within a working Flask app.
Our table has just two columns, one of which shows the name and is a
link to the item's page. The other shows the description.
"""

app = Flask(__name__)
Bootstrap(app)


class ItemTable(Table):
    city = Col('City')
    sell_price_min = Col('Sell_Price_Min')


@app.route('/')
def index():
    items = Item.get_elements()
    table = ItemTable(items)

    # You would usually want to pass this out to a template with
    # render_template.
    return render_template('index.html', table=table)


@app.route('/item/<int:id>')
def single_item(id):
    element = Item.get_element_by_id(id)
    # Similarly, normally you would use render_template
    return '<h1>{}</h1><p>{}</p><hr><small>id: {}</small>'.format(
        element.city, element.sell_price_min)


class Item(object):
    """ a little fake database """

    def __init__(self, city, sell_price_min):
        self.city = city
        self.sell_price_min = sell_price_min

    @classmethod
    def get_elements(cls):
        with open('../json/TestItems.json') as jsonFile:
            items = json.load(jsonFile)

            for item in items['items']:
                url = 'https://www.albion-online-data.com/api/v1/stats/Prices/' + item['name'] + '?'
                response = requests.get(url, timeout=10)
                objects = response.json()
            return objects

    @classmethod
    def get_element_by_id(cls, id):
        return [i for i in cls.get_elements() if i.id == id][0]


if __name__ == '__main__':
    app.run(debug=True)
